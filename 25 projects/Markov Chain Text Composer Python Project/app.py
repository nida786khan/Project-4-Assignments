import streamlit as st
import markovify

# Streamlit UI
st.title("🎵 Markov Chain Text Composer")

# User Input
st.sidebar.header("Upload Text File")
uploaded_file = st.sidebar.file_uploader("Upload a text file", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    
    # Train Markov Model
    text_model = markovify.Text(text, state_size=2)

    # Generate Text
    st.sidebar.header("Generate Text")
    sentence_count = st.sidebar.slider("Number of Sentences", 1, 5, 3)

    if st.sidebar.button("Generate"):
        st.write("### 🎶 Generated Text:")
        for _ in range(sentence_count):
            st.write(text_model.make_sentence())

