# 🤖 InspAIct – Intelligent Bottle Defect Detection with PatchCore & MVTec AD  

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#)  
[![Streamlit Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?logo=streamlit)](https://sachiin044-bottles-defect-detection-project-srcapp-zoypv0.streamlit.app/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)  
![Status](https://img.shields.io/badge/Status-Active-success)  

**InspAIct** is a **Streamlit-powered anomaly detection app** that uses the **PatchCore** algorithm to identify manufacturing defects in bottles from the **MVTec AD** dataset.  
It detects issues like cracks, contamination, and broken seals — with **heatmap visualizations** to make defects easy to spot.  

---

## 📑 Table of Contents
1. [Project Overview](#1️⃣-project-overview)  
2. [Motivation](#2️⃣-motivation)  
3. [Features](#3️⃣-features)  
4. [Tech Stack](#4️⃣-tech-stack)  
5. [Live Demo](#5️⃣-live-demo)  
6. [Installation](#6️⃣-installation)  
7. [Usage](#7️⃣-usage)  
8. [Input & Output Format](#8️⃣-input--output-format)  
9. [Project Structure](#9️⃣-project-structure)  
10. [Dataset](#-dataset)  
11. [Model Details](#1️⃣1️⃣-model-details)  
12. [Results & Examples](#1️⃣2️⃣-results--examples)  
13. [Why It Matters](#1️⃣3️⃣-why-it-matters)  
14. [Future Work / Roadmap](#1️⃣4️⃣-future-work--roadmap)  
15. [Contributing](#1️⃣5️⃣-contributing)  
16. [License](#1️⃣6️⃣-license)  
17. [Acknowledgements](#1️⃣7️⃣-acknowledgements)  
18. [Contact](#1️⃣8️⃣-contact)  

---

## 1️⃣ Project Overview

**InspAIct** is designed to assist in **quality control** for bottling lines by providing:
- Fast detection of visual defects
- Clear anomaly localization with heatmaps
- An easy-to-use web interface for real-time inspection

Built on **PatchCore** anomaly detection, this tool focuses on **bottle inspection** but can be extended to other industrial objects from MVTec AD.

---

## 2️⃣ Motivation

In the beverage and packaging industry, even minor defects can lead to:
- **Product recalls**
- **Customer dissatisfaction**
- **Increased waste and costs**

Large-scale defect detection systems can be expensive and require specialized hardware.  
**InspAIct** makes **AI-driven inspection** accessible:
- Runs in the cloud or locally
- Minimal setup with a simple Streamlit app
- Uses open-source models and datasets

---

## 3️⃣ Features

- ✅ Detects anomalies in **bottle images**
- 🔥 Generates **pixel-level anomaly heatmaps**
- 🖼 Displays **original image** side-by-side with the heatmap
- 📊 Shows **predicted label** and **anomaly score**
- ☁️ Deployable to **Streamlit Cloud** for instant demo access

---

## 4️⃣ Tech Stack

- **Framework:** [Streamlit](https://streamlit.io/)
- **Anomaly Detection Model:** [PatchCore](https://arxiv.org/abs/2106.08265)
- **Dataset:** [MVTec AD – Bottle](https://www.mvtec.com/company/research/datasets/mvtec-ad)
- **Languages:** Python
- **Libraries:** NumPy, Pandas, Pillow, PyTorch, Matplotlib

---

## 5️⃣ Live Demo

🚀 **Try it online:** [Run InspAIct on Streamlit Cloud](https://sachiin044-bottles-defect-detection-project-srcapp-zoypv0.streamlit.app/)  

---

## 6️⃣ Installation

1. **Clone the repository**
```bash
git clone https://github.com/sachiin044/bottles_defect_detection_project.git
cd bottles_defect_detection_project
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 7️⃣ Usage

**Run Locally**
```bash
streamlit run src/app.py
```

**Run on Streamlit Cloud**
This project is already deployed online:  
[Click here to try InspAIct now](https://sachiin044-bottles-defect-detection-project-srcapp-zoypv0.streamlit.app/)

---

## 8️⃣ Input & Output Format

**Input:**
   - A test image from the MVTec AD bottle dataset.

**Output:**
   - Anomaly heatmap highlighting defect regions.
   - Predicted label (Normal / Defective).
   - Anomaly score (numeric confidence).

**Example:**
```bash
Image: broken_large/000.png
Predicted Label: defective
Anomaly Score: 0.92
```

---

**9️⃣ Project Structure**
```bash
bottles_defect_detection_project/
│
├── src/
│   └── app.py                # Streamlit frontend
│
├── results/
│   ├── predictions.csv       # Inference results
│   ├── confusion_matrix.png
│   ├── heatmaps/              # Generated anomaly heatmaps
│   └── originals/             # Original test images
│
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---

## 🔟 Dataset
   - **Name:** MVTec AD – Bottle category
   - **Description:** Contains normal and defective bottle images for anomaly detection.
   - **Source:** https://www.mvtec.com/company/research/datasets/mvtec-ad
   - **Usage in this project:** Used for evaluating and visualizing PatchCore’s bottle defect detection performance.

---

## 1️⃣1️⃣ Model Details

- **Algorithm:** PatchCore (Anomaly detection using patch-based features)  
- **Framework:** PyTorch  
- **Input Size:** Configured for MVTec AD bottle images  
- **Training:** Pre-trained on MVTec AD training split (normal images only)  
- **Inference:** Produces both a binary prediction (Normal/Defective) and a pixel-level anomaly map  

---

## 1️⃣2️⃣ Results & Examples

| Defect Type  | Example Image | Heatmap | Predicted Label | Anomaly Score |
|--------------|--------------|---------|----------------|---------------|
| Broken Large | ![original](results/originals/broken_large/000.png) | ![heatmap](results/broken_large_000.png) | Defective | 0.92 |

The heatmap clearly highlights defect regions, enabling easy visual verification.

---

## 1️⃣3️⃣ Why It Matters

In beverage manufacturing, **quality control** is essential to maintain:
- **Product safety**
- **Customer trust**
- **Regulatory compliance**

Automated defect detection with **InspAIct**:
- Reduces inspection time and costs  
- Minimizes human error in visual inspection  
- Enables quick identification of recurring production issues  

---

## 1️⃣4️⃣ Future Work / Roadmap

- [ ] Add **real-time image upload** for live scoring  
- [ ] Extend support to **other MVTec AD classes** (e.g., screw, hazelnut, cable)  
- [ ] Implement **batch inference mode**  
- [ ] Generate **detailed PDF reports** of inspection results  
- [ ] Add **user authentication** and session tracking in the app  

---

## 1️⃣5️⃣ Contributing

We welcome contributions!  
To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes and push the branch.
4. Open a Pull Request.

Please check our **[CONTRIBUTING.md](CONTRIBUTING.md)** for guidelines.

---

## 1️⃣6️⃣ License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it for both personal and commercial purposes, provided proper attribution is given.  
See the [LICENSE](LICENSE) file for full details.

---

## 1️⃣7️⃣ Acknowledgements

- **PatchCore**: [https://arxiv.org/abs/2106.08265](https://arxiv.org/abs/2106.08265) – Base anomaly detection algorithm.
- **MVTec AD Dataset**: [https://www.mvtec.com/company/research/datasets/mvtec-ad](https://www.mvtec.com/company/research/datasets/mvtec-ad) – Source of training and testing images.
- **Streamlit**: [https://streamlit.io/](https://streamlit.io/) – Web app framework for interactive demos.
- The open-source AI community for tools, inspiration, and resources.

---

## 1️⃣8️⃣ Contact

**Author:** Sachin Gupta  
**GitHub:** [@sachiin044](https://github.com/sachiin044)  
**Email:** royalsachingupta@gmail.com  
**LinkedIn:** [sachiin04](https://www.linkedin.com/in/sachiin04)  
**Live Demo:** [InspAIct on Streamlit](https://sachiin044-bottles-defect-detection-project-srcapp-zoypv0.streamlit.app/)  








