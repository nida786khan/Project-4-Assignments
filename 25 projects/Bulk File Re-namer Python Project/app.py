import streamlit as st
import os
import shutil
from PIL import Image

# Set Streamlit page config
st.set_page_config(page_title="Bulk Image Renamer", layout="centered")

st.title("📂 Bulk Image Renamer with Drag & Drop")

st.write("### Drag and drop images here")
uploaded_files = st.file_uploader("Upload Images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

prefix = st.text_input("Enter Prefix for Renaming", "image_")
rename_button = st.button("Rename Images")

if rename_button and uploaded_files:
    output_dir = "renamed_images"
    os.makedirs(output_dir, exist_ok=True)
    
    for index, uploaded_file in enumerate(uploaded_files):
        file_extension = os.path.splitext(uploaded_file.name)[1]  # Get file extension
        new_filename = f"{prefix}{index + 1}{file_extension}"
        file_path = os.path.join(output_dir, new_filename)

        # Save file
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

    st.success(f"✅ Renamed {len(uploaded_files)} images successfully!")
    st.download_button("Download Renamed Files", output_dir, "renamed_images.zip", "application/zip")

st.markdown("Developed by *Nida Khan*")
