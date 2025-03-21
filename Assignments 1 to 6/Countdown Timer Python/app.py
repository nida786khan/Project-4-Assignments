import streamlit as st
import time

# Streamlit UI
st.title("⏳ Countdown Timer")

# User input for countdown time
seconds = st.number_input("Enter countdown time (in seconds):", min_value=1, step=1)

if st.button("Start Timer ⏰"):
    with st.empty():
        for remaining in range(seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            st.write(f"⏳ **Time Left: {mins:02d}:{secs:02d}**")
            time.sleep(1)
        st.write("⏰ **Time's up! 🎉**")

