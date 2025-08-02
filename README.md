# 🧪 Bottles Defect Detection with PatchCore & MVTec AD

A lightweight, anomaly detection web app using **PatchCore** and the **MVTec AD "bottle" dataset**.  
It detects visual defects like cracks, contamination, and broken seals — deployed on **Streamlit Cloud** for instant demo access.

---

## 🚀 Live Demo

🔗 [Click here to run the app on Streamlit](https://sachiin044-bottles-defect-detection-project-srcapp-zoypv0.streamlit.app/)

---

## 📦 Features

- ✅ Detects and classifies anomalies in bottle images
- 🔥 Shows **pixel-wise anomaly heatmap**
- 🖼 Displays **original test image** *(if available)*
- 📊 Summarizes **predicted labels, scores**
- ☁️ Fully deployed on **Streamlit Cloud** — no install needed

---

## 🖼 Sample Output

| Original Image | Heatmap |
|----------------|---------|
| ![original](results/originals/broken_large/000.png) | ![heatmap](results/broken_large_000.png) |

---

defect_detection_project/
├── src/
│ └── app.py # Streamlit frontend
├── results/
│ ├── predictions.csv # Inference results
│ ├── confusion_matrix.png
│ ├── heatmaps/
│ └── originals/
├── requirements.txt
└── README.md

## 📁 Project Structure

