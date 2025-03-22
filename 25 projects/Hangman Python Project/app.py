import streamlit as st
import random

st.title("🔠💀 Hangman Game")

# Initialize session state
if "word" not in st.session_state:
    st.session_state.word = random.choice(["python", "hangman", "developer", "programming", "challenge"])
    st.session_state.guessed_letters = set()
    st.session_state.attempts = 6
    st.session_state.word_display = ["_"] * len(st.session_state.word)

st.write(" ".join(st.session_state.word_display))
st.write(f"Remaining attempts: {st.session_state.attempts}")

guess = st.text_input("Guess a letter: ", max_chars=1).lower()

if st.button("Submit Guess"):
    if guess in st.session_state.guessed_letters:
        st.warning("⚠ You already guessed that letter.")
    elif guess in st.session_state.word:
        st.success("✅ Correct!")
        for index, letter in enumerate(st.session_state.word):
            if letter == guess:
                st.session_state.word_display[index] = guess
    else:
        st.error("❌ Wrong guess!")
        st.session_state.attempts -= 1
    
    st.session_state.guessed_letters.add(guess)

# Check for win or lose
if "_" not in st.session_state.word_display:
    st.success(f"🎉 You won! The word was **{st.session_state.word}**.")
    st.session_state.word = random.choice(["python", "hangman", "developer", "programming", "challenge"])  # Reset game
    st.session_state.guessed_letters = set()
    st.session_state.attempts = 6
    st.session_state.word_display = ["_"] * len(st.session_state.word)
elif st.session_state.attempts == 0:
    st.error(f"💀 Game over! The word was **{st.session_state.word}**.")
    st.session_state.word = random.choice(["python", "hangman", "developer", "programming", "challenge"])  # Reset game
    st.session_state.guessed_letters = set()
    st.session_state.attempts = 6
    st.session_state.word_display = ["_"] * len(st.session_state.word)
