import streamlit as st
import random

st.title("🤖 Computer Guess the Number Game")

# Initialize session state
if "low" not in st.session_state:
    st.session_state.low, st.session_state.high = 1, 100
    st.session_state.guess = random.randint(1, 100)
    st.session_state.attempts = 0

st.write(f"Computer's guess: **{st.session_state.guess}**")

# User feedback buttons
col1, col2, col3 = st.columns(3)
if col1.button("Too High ⬆"):
    st.session_state.high = st.session_state.guess - 1
elif col2.button("Too Low ⬇"):
    st.session_state.low = st.session_state.guess + 1
elif col3.button("Correct ✅"):
    st.success(f"🎉 Yay! Computer guessed the number {st.session_state.guess} in {st.session_state.attempts + 1} attempts!")
    st.session_state.low, st.session_state.high = 1, 100  # Reset game
    st.session_state.guess = random.randint(1, 100)
    st.session_state.attempts = 0

# Update guess
if st.session_state.low <= st.session_state.high:
    st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
    st.session_state.attempts += 1
