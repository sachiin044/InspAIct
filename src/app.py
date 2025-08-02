# src/app.py

import streamlit as st
import os
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Defect Detection App", layout="wide")
st.title("🔍 Defect Detection with PatchCore")
st.markdown("Visualize anomaly predictions and heatmaps for MVTec AD test images.")

# === CONFIGURATION ===
PREDICTIONS_CSV = "results/predictions.csv"
HEATMAP_DIR = "results"
TEST_IMAGE_DIR = "./results/originals"

# === Load Predictions ===
@st.cache_data
def load_predictions():
    if os.path.exists(PREDICTIONS_CSV):
        return pd.read_csv(PREDICTIONS_CSV)
    return pd.DataFrame()

df = load_predictions()

# === Sidebar Controls ===
st.sidebar.header("Choose Defect Type")
if not df.empty:
    defect_types = sorted(df["Defect_Type"].unique())
    selected_defect = st.sidebar.selectbox("Defect Type", defect_types)

    filtered = df[df["Defect_Type"] == selected_defect]
    image_names = filtered["Image"].tolist()
    selected_image = st.sidebar.selectbox("Test Image", image_names)

    row = filtered[filtered["Image"] == selected_image].iloc[0]

    # === Paths ===
    original_path = os.path.join(TEST_IMAGE_DIR, selected_defect, selected_image)
    heatmap_path = os.path.join(HEATMAP_DIR, f"{selected_defect}_{selected_image}")

    # === Display Images Side by Side ===
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧪 Original Test Image")
        if os.path.exists(original_path):
            st.image(Image.open(original_path), use_container_width=True)
        else:
            st.warning("Original image not found.")

    with col2:
        st.subheader("🔥 Predicted Heatmap")
        if os.path.exists(heatmap_path):
            st.image(Image.open(heatmap_path), use_container_width=True)
        else:
            st.warning("Heatmap not found.")

    # === Prediction Info ===
    st.markdown("---")
    st.subheader("📋 Prediction Summary")
    st.markdown(f"""
    - **File**: `{selected_image}`
    - **Defect Type**: `{row['Defect_Type']}`
    - **Predicted Label**: `{row['Predicted_Label']}`
    - **Anomaly Score**: `{row['Anomaly_Score']}`
    """)
else:
    st.warning("⚠️ No predictions found. Please run `run_inference.py` first.")
