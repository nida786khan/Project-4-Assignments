import streamlit as st
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

st.title("Random Password Generator")

num_passwords = st.number_input("Enter number of passwords:", min_value=1, value=5)
password_length = st.number_input("Enter password length:", min_value=4, value=8)

if st.button("Generate"):
    st.write("## Generated Passwords:")
    for _ in range(num_passwords):
        st.code(generate_password(password_length))
