import streamlit as st
import time

st.title("⏳ Countdown Timer")

# Get user input
seconds = st.number_input("Enter time in seconds:", min_value=1, step=1)

# Timer control variables
stop_timer = st.checkbox("Stop Timer")  # Stop functionality
start = st.button("Start Timer")

if start:
    progress_bar = st.progress(0)  # Progress bar
    with st.empty():
        for remaining in range(seconds, -1, -1):
            if stop_timer:
                st.warning("⏹ Timer Stopped!")
                break  # Exit loop if stop is pressed
            mins, secs = divmod(remaining, 60)
            st.subheader(f"⏳ {mins:02}:{secs:02}")
            progress_bar.progress((seconds - remaining) / seconds)  
            time.sleep(1)
        else:
            st.success("⏰ Time's up!")

