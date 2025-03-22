import streamlit as st
import random

st.title("🎲 Guess the Number Game")

# Initialize session state variables
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0

# User input
guess = st.number_input("Guess a number between 1 and 100", min_value=1, max_value=100, step=1)

if st.button("Check Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.warning("Too low! Try again. ⬆")
    elif guess > st.session_state.secret_number:
        st.warning("Too high! Try again. ⬇")
    else:
        st.success(f"🎉 Congratulations! You guessed the number {st.session_state.secret_number} in {st.session_state.attempts} attempts.")
        st.session_state.secret_number = random.randint(1, 100)  # Reset game
        st.session_state.attempts = 0
