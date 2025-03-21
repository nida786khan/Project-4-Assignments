import streamlit as st

st.title("🎭 Mad Libs Game")
st.write("Fill in the blanks to create your own fun story!")

# User Inputs
adjective = st.text_input("Enter an adjective:")
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
place = st.text_input("Enter a place:")

# Generate story on button click
if st.button("Generate Story"):
    if adjective and noun and verb and place:
        story = f"One day, a {adjective} {noun} decided to {verb} at {place}. It was a fantastic adventure! 🎉"
        st.success("Here is your Mad Libs story:")
        st.write(story)
    else:
        st.warning("⚠️ Please fill in all the blanks before generating the story.")

