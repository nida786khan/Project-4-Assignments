import streamlit as st
import random

# Session state me game variables store karein
if "word" not in st.session_state:
    st.session_state.word = random.choice(["apple", "banana", "grape", "orange", "mango"])
    st.session_state.hidden_word = ["_"] * len(st.session_state.word)
    st.session_state.attempts = 6
    st.session_state.guessed_letters = []

st.title("🎯 Hangman Game")
st.write("Guess the word letter by letter!")

# Display hidden word
st.write(" ".join(st.session_state.hidden_word))
st.write(f"Remaining attempts: {st.session_state.attempts}")

# User se letter input lena
guess = st.text_input("Guess a letter:", max_chars=1).lower()

if st.button("Submit Guess"):
    if guess in st.session_state.guessed_letters:
        st.warning("⚠️ You already guessed that letter!")
    elif guess in st.session_state.word:
        st.session_state.guessed_letters.append(guess)
        for i, letter in enumerate(st.session_state.word):
            if letter == guess:
                st.session_state.hidden_word[i] = guess
        st.success("✅ Correct guess!")
    else:
        st.session_state.guessed_letters.append(guess)
        st.session_state.attempts -= 1
        st.error("❌ Wrong guess!")

    # Win/Loss Check
    if "_" not in st.session_state.hidden_word:
        st.balloons()
        st.success(f"🎉 You won! The word was '{st.session_state.word}'.")
        st.session_state.word = random.choice(["apple", "banana", "grape", "orange", "mango"])
        st.session_state.hidden_word = ["_"] * len(st.session_state.word)
        st.session_state.attempts = 6
        st.session_state.guessed_letters = []

    if st.session_state.attempts == 0:
        st.error(f"💀 Game Over! The word was '{st.session_state.word}'.")
        st.session_state.word = random.choice(["apple", "banana", "grape", "orange", "mango"])
        st.session_state.hidden_word = ["_"] * len(st.session_state.word)
        st.session_state.attempts = 6
        st.session_state.guessed_letters = []
