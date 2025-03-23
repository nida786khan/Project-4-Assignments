import random
import streamlit as st

# Game Title
st.title("🎯 Fun Number Guessing Game")

# Game Instructions
st.markdown("""
🔹 I have chosen a number between **1 and 100**.  
🔹 You have **5 chances** to guess it.  
🔹 I will give hints if you are **too close** or **too far**!  
🎮 Let's Play!
""")

# Random number generate karna
random_number = random.randint(1, 100)

# Session state to track attempts
if "attempts" not in st.session_state:
    st.session_state.attempts = 5

# User input
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, value=1)

# Check button
if st.button("Check Guess"):
    if st.session_state.attempts > 0:
        st.session_state.attempts -= 1

        if user_guess == random_number:
            st.success(f"🎉 Amazing! You guessed the number {random_number} correctly in {5 - st.session_state.attempts} tries!")
            st.balloons()
            st.session_state.attempts = 0  # Game Over

        elif abs(user_guess - random_number) <= 5:
            st.warning("🔥 Very Close! Try again.")
        elif abs(user_guess - random_number) <= 15:
            st.warning("😬 A little close, but not quite.")
        else:
            st.warning("❄️ Too far! Try a better guess.")

        if st.session_state.attempts == 0 and user_guess != random_number:
            st.error(f"😢 Oh no! You're out of attempts. The correct number was {random_number}.")
    
    else:
        st.error("Game Over! Refresh to play again.")
