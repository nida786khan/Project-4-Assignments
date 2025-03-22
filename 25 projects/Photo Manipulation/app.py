import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

# Streamlit UI
st.title("📸 Photo Manipulation App")

# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Filters
    st.sidebar.header("Adjustments")
    brightness = st.sidebar.slider("Brightness", 0.5, 2.0, 1.0)
    contrast = st.sidebar.slider("Contrast", 0.5, 2.0, 1.0)
    blur = st.sidebar.slider("Blur", 0, 10, 0)

    # Apply Effects
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)

    if blur > 0:
        image = image.filter(ImageFilter.GaussianBlur(blur))

    # Show Processed Image
    st.image(image, caption="Processed Image", use_column_width=True)

    # Download Button
    st.sidebar.download_button("Download Edited Image", image.tobytes(), file_name="edited_image.png")
