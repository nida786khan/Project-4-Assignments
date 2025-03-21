import streamlit as st
import random

# Define choices
options = ["rock", "paper", "scissors"]

# Streamlit UI
st.title("🪨📄✂️ Rock, Paper, Scissors Game!")

# Store the user's choice in session state
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None
if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = None
if "result" not in st.session_state:
    st.session_state.result = None

st.write("Choose Rock, Paper, or Scissors:")

# Create buttons for user choices
col1, col2, col3 = st.columns(3)

if col1.button("🪨 Rock"):
    st.session_state.user_choice = "rock"
if col2.button("📄 Paper"):
    st.session_state.user_choice = "paper"
if col3.button("✂️ Scissors"):
    st.session_state.user_choice = "scissors"

# If user made a choice, generate computer choice and determine the result
if st.session_state.user_choice:
    st.session_state.computer_choice = random.choice(options)

    if st.session_state.user_choice == st.session_state.computer_choice:
        st.session_state.result = "🤝 It's a tie!"
    elif (st.session_state.user_choice == "rock" and st.session_state.computer_choice == "scissors") or \
         (st.session_state.user_choice == "paper" and st.session_state.computer_choice == "rock") or \
         (st.session_state.user_choice == "scissors" and st.session_state.computer_choice == "paper"):
        st.session_state.result = "🎉 You win!"
    else:
        st.session_state.result = "😢 You lose!"

# Display results
if st.session_state.user_choice:
    st.write(f"**Your choice:** {st.session_state.user_choice.capitalize()}")
    st.write(f"**Computer's choice:** {st.session_state.computer_choice.capitalize()}")
    st.subheader(st.session_state.result)

# Restart button
if st.button("🔄 Play Again"):
    st.session_state.user_choice = None
    st.session_state.computer_choice = None
    st.session_state.result = None
    st.experimental_rerun()
