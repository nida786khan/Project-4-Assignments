import streamlit as st
import random

# Session state me number store karna (Ek hi number bar bar change na ho)
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 10)

st.title("🎯 Guess the Number Game")
st.write("Guess a number between **1 and 10**.")

# User input lene ke liye text_input use karein
guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

# Guess button
if st.button("Check"):
    if guess == st.session_state.number:
        st.success("🎉 Correct! You guessed it right.")
        # Naya number generate karna
        st.session_state.number = random.randint(1, 10)
    else:
        st.error("❌ Wrong! Try again.")

