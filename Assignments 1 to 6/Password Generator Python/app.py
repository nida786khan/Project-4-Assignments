import streamlit as st
import random
import string

# Function to generate password
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit UI
st.title("🔐 Password Generator")
st.write("Generate a secure password instantly!")

# User input for password length
length = st.number_input("Enter password length:", min_value=4, max_value=32, value=8, step=1)

# Generate password on button click
if st.button("Generate Password"):
    password = generate_password(length)
    st.success(f"Generated Password: `{password}`")
