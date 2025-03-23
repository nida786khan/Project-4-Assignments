import streamlit as st

# Streamlit UI
st.title("🎵 Markov Chain Text Composer")

# User Input
st.sidebar.header("Upload a Text File")
uploaded_file = st.sidebar.file_uploader("Upload a text file", type=["txt"])

if uploaded_file:
    # Read & Decode Text File
    text = uploaded_file.read().decode("utf-8")

    # Check if the file is empty
    if not text.strip():
        st.error("❌ Error: The uploaded file is empty. Please upload a valid text file.")
    else:
        st.write("### 📜 Extracted Text:")
        st.text_area("Extracted Content:", text, height=300)

