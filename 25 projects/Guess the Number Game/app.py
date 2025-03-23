import random
import streamlit as st

# Page Title
st.title("🤖 Computer Guessing Game")

st.markdown("""
🔹 Think of a number between **1 and 100** in your mind.  
🔹 The computer will try to guess it.  
🔹 Click **Too High (H), Too Low (L), or Correct (C)** to guide the computer.  
🔹 **Computer gets points:**  
   - ✅ **Correct Guess:** +1 Point  
   - ❌ **Wrong Guess:** -1 Point  
   - 🏆 **Let's see how well the computer plays!**  
""")

# Initialize game state
if "low" not in st.session_state:
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
    st.session_state.score = 0  # Score Tracking
    st.session_state.last_feedback = ""  # Store last feedback

# Display current guess
st.write(f"🤔 Computer's Guess: **{st.session_state.guess}**")

# Buttons for user feedback
col1, col2, col3 = st.columns(3)

# Too High (H) Button
if col1.button("⬆️ Too High (H)"):
    if st.session_state.guess < st.session_state.low:  # Wrong move (Should have been low)
        st.session_state.score -= 1
        st.error("❌ Computer made a wrong move! -1 Point")
    else:
        st.session_state.high = st.session_state.guess - 1
        st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)

# Too Low (L) Button
if col2.button("⬇️ Too Low (L)"):
    if st.session_state.guess > st.session_state.high:  # Wrong move (Should have been high)
        st.session_state.score -= 1
        st.error("❌ Computer made a wrong move! -1 Point")
    else:
        st.session_state.low = st.session_state.guess + 1
        st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)

# Correct (C) Button
if col3.button("✅ Correct (C)"):
    st.session_state.score += 1  # Increase score for correct guess
    st.success(f"🎉 Yay! The computer guessed your number **{st.session_state.guess}** correctly!")
    st.balloons()

    # Reset game
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)

# Show Score
st.write(f"🏆 **Computer's Score: {st.session_state.score}**")
