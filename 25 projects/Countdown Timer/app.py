import streamlit as st
import time

st.title("⏳ Countdown Timer")

# Initialize session state variables
if 'remaining_time' not in st.session_state:
    st.session_state.remaining_time = 1  # Ensuring it's at least 1
if 'running' not in st.session_state:
    st.session_state.running = False

# Get user input for countdown
seconds = st.number_input("Enter time in seconds:", min_value=1, step=1, value=max(st.session_state.remaining_time, 1))

# Buttons for controls
col1, col2, col3, col4 = st.columns(4)
start = col1.button("Start")
stop = col2.button("Stop")
resume = col3.button("Resume")
clear = col4.button("Clear")

# Start Timer
if start:
    st.session_state.remaining_time = seconds
    st.session_state.running = True

# Stop Timer
if stop:
    st.session_state.running = False  # Stop the countdown but keep the current time

# Resume Timer
if resume:
    st.session_state.running = True

# Clear Timer (Removes everything)
if clear:
    st.session_state.running = False
    st.session_state.remaining_time = 1
    st.rerun()  # Refresh the app

# Timer logic
progress_bar = st.progress(0)
timer_display = st.empty()  # Store timer text separately

if st.session_state.running and st.session_state.remaining_time > 0:
    for remaining in range(st.session_state.remaining_time, -1, -1):
        if not st.session_state.running:
            st.session_state.remaining_time = remaining  # Save the stopped time
            break  # Stop the loop without removing display

        mins, secs = divmod(remaining, 60)
        timer_display.subheader(f"⏳ {mins:02}:{secs:02}")
        progress_bar.progress((seconds - remaining) / seconds)
        time.sleep(1)

    else:
        st.success("⏰ Time's up!")
        st.session_state.running = False

if not st.session_state.running and not clear:
    mins, secs = divmod(st.session_state.remaining_time, 60)
    timer_display.subheader(f"⏹ Timer Stopped at {mins:02}:{secs:02}")
