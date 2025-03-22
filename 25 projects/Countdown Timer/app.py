import streamlit as st
import time

st.title("⏳ Countdown Timer")

# Get user input
seconds = st.number_input("Enter time in seconds:", min_value=1, step=1)

if st.button("Start Timer"):
    with st.empty():
        for remaining in range(seconds, -1, -1):
            mins, secs = divmod(remaining, 60)
            st.subheader(f"⏳ {mins:02}:{secs:02}")
            time.sleep(1)
        st.success("⏰ Time's up!")
