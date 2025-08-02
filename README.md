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

## 📁 Project Structure
defect_detection_project/
- ├── src/
- │ └── app.py # Streamlit frontend
- ├── results/
- │ ├── predictions.csv # Inference results
- │ ├── confusion_matrix.png
- │ ├── heatmaps/
- │ └── originals/
- ├── requirements.txt
- └── README.md
## 🧑‍💻 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/sachiin044/bottles_defect_detection_project.git
   cd bottles_defect_detection_project
   
2. Create virtual environment (optional but recommended)
  python -m venv venv
  source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies
   pip install -r requirements.txt
   
4. Run Streamlit app
   streamlit run src/app.py

## 🤝 Collaborators Welcome!

Want to contribute? Awesome!
- 🍴 Fork this repo
- 🌿 Create a new branch (git checkout -b feature-name)
- 📦 Add your code
- 📩 Submit a pull request


🧠 Future Ideas (Open to Contribution)
- 📸 Add image upload and live scoring
- 🧠 Support other MVTec classes (screw, cable, hazelnut...)
- 📤 Export results to PDF
- 🌐 Add login / session tracking

## 👨‍💻 Author
Sachin Gupta
📧 Email: royalsachingupta@gmail.com
🔗 GitHub: @sachiin044

## 📜 License
MIT License. Feel free to use, modify, and distribute ⭐


