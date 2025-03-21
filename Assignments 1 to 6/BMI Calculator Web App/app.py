import streamlit as st

st.title("BMI Calculator")
st.write("Enter your details below:")

# User input
weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (m)", min_value=0.5, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
    else:
        st.write("Please enter a valid height.")
