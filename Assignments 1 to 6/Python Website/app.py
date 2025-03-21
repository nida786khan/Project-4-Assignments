import streamlit as st

# Website Title
st.title("Welcome to My Streamlit Website! 🚀")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Home Page
if page == "Home":
    st.header("Home Page")
    st.write("This is a simple website built with **Streamlit** in Python.")
    st.image("https://source.unsplash.com/800x400/?technology", caption="Tech Image")

# About Page
elif page == "About":
    st.header("About Me")
    st.write("Hello! My name is **Nida**, and I'm learning Streamlit to build amazing web apps. 💻")

# Contact Page
elif page == "Contact":
    st.header("Contact Me")
    name = st.text_input("Enter your name:")
    message = st.text_area("Your message:")
    if st.button("Send Message"):
        st.success(f"Thanks, {name}! Your message has been received.")

# Footer
st.write("---")
st.write("© 2024 - Made with ❤️ by Nida")