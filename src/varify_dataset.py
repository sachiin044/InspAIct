# src/verify_dataset.py

import os

def count_images(folder):
    total = 0
    for root, _, files in os.walk(folder):
        imgs = [f for f in files if f.endswith(('.png', '.jpg'))]
        total += len(imgs)
        if imgs:
            print(f"{root}: {len(imgs)} images")
    return total

if __name__ == "__main__":
    root_path = "mvtec_ad/bottle"
    total = count_images(root_path)
    print(f"\n✅ Total images in dataset: {total}")
