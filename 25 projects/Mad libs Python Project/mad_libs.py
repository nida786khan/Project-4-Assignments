import streamlit as st

# Title of the app
st.title("🎭 Fun Mad Libs Game")

# User inputs
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
adjective = st.text_input("Enter an adjective:")
place = st.text_input("Enter a place:")

# Generate Mad Libs story
if st.button("Generate Story"):
    story = f"One day, a {adjective} {noun} decided to {verb} at the {place}. It was the best adventure ever!"
    st.subheader("Here is your Mad Libs Story:")
    st.write(story)
