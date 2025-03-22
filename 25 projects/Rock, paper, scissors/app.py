import streamlit as st
import random

st.title("✊📄✂ Rock, Paper, Scissors Game")

options = ["rock", "paper", "scissors"]
user_choice = st.radio("Choose your move:", options)

if st.button("Play"):
    computer_choice = random.choice(options)
    st.write(f"🤖 Computer chose: **{computer_choice}**")

    if user_choice == computer_choice:
        st.info("It's a tie! 😐")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        st.success("🎉 You win! 🎊")
    else:
        st.error("😢 You lose! Better luck next time.")
