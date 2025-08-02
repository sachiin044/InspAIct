# src/evaluate.py

import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load predictions
csv_path = "results/predictions.csv"
df = pd.read_csv(csv_path)

# Ground truth: label = "normal" if type == good, else "anomaly"
df["GroundTruth"] = df["Defect_Type"].apply(lambda x: "normal" if x == "good" else "anomaly")

# Evaluation
y_true = df["GroundTruth"]
y_pred = df["Predicted_Label"]

# Print metrics
print("✅ Classification Report:\n")
print(classification_report(y_true, y_pred, digits=4))

# Optional: Confusion Matrix
cm = confusion_matrix(y_true, y_pred, labels=["normal", "anomaly"])

# Plot confusion matrix
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["normal", "anomaly"], yticklabels=["normal", "anomaly"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.savefig("results/confusion_matrix.png")
print("\n📊 Confusion matrix saved as 'results/confusion_matrix.png'")
