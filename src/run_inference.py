# src/run_inference.py

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import sys
import numpy as np
from PIL import Image
from tqdm import tqdm
import torch
from torchvision import transforms
import cv2
import csv

# Add PatchCore to Python path
patchcore_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../patchcore-inspection/src"))
sys.path.insert(0, patchcore_path)

from patchcore.patchcore import PatchCore
import patchcore.backbones as backbones

# === CONFIGURATION ===
DATASET_PATH = "mvtec_ad/bottle"
RESULTS_PATH = "results"
DEVICE = torch.device("cpu")
IMAGE_SIZE = 256

# === Create output directory ===
os.makedirs(RESULTS_PATH, exist_ok=True)

# === Load PatchCore Model ===
backbone, feat_dims = backbones.load("resnet18")
model = PatchCore(device=DEVICE)
model.load(
    backbone=backbone,
    layers_to_extract_from=["layer2", "layer3"],
    device=DEVICE,
    input_shape=(3, IMAGE_SIZE, IMAGE_SIZE),
    pretrain_embed_dimension=feat_dims,
    target_embed_dimension=1024,
)

# === Image Preprocessing ===
transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
])

# === Step 1: Fit on train/good ===
train_dir = os.path.join(DATASET_PATH, "train", "good")
train_images = [
    os.path.join(train_dir, f)
    for f in os.listdir(train_dir)
    if f.endswith(".png")
]

train_data = []
for path in tqdm(train_images, desc="Fitting PatchCore on train/good"):
    img = Image.open(path).convert("RGB")
    img_tensor = transform(img).unsqueeze(0).to(DEVICE)  # Shape: (1, 3, 256, 256)
    train_data.append(img_tensor)

model.fit(train_data)

# === Step 2: Inference on test images ===
test_dir = os.path.join(DATASET_PATH, "test")
results_csv = []

for defect_type in sorted(os.listdir(test_dir)):
    defect_folder = os.path.join(test_dir, defect_type)
    if not os.path.isdir(defect_folder):
        continue

    for fname in tqdm(os.listdir(defect_folder), desc=f"Testing {defect_type}"):
        if not fname.endswith(".png"):
            continue

        img_path = os.path.join(defect_folder, fname)
        img = Image.open(img_path).convert("RGB")
        img_tensor = transform(img).unsqueeze(0).to(DEVICE)

        with torch.no_grad():
            score, heatmap = model.predict(img_tensor)

        # Predicted label
        label = "anomaly" if defect_type != "good" else "normal"

        # === Save heatmap ===
        heatmap_tensor = heatmap[0].squeeze()  # already numpy
        heatmap_img = (heatmap_tensor * 255).astype(np.uint8)
        heatmap_color = cv2.applyColorMap(heatmap_img, cv2.COLORMAP_JET)

        save_path = os.path.join(RESULTS_PATH, f"{defect_type}_{fname}")
        cv2.imwrite(save_path, heatmap_color)

        # === Save CSV row ===
        results_csv.append([fname, defect_type, label, round(score[0], 4)])  # ✅ Fix: score is a list

# === Step 3: Save predictions.csv ===
csv_path = os.path.join(RESULTS_PATH, "predictions.csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Image", "Defect_Type", "Predicted_Label", "Anomaly_Score"])
    writer.writerows(results_csv)

print(f"\n✅ Inference complete. Heatmaps and CSV saved to '{RESULTS_PATH}/'")
