import streamlit as st

# Hardcoded weather data for a specific city
weather_data = {
    "London": {
        "Temperature": "15°C",
        "Weather": "Cloudy",
        "Humidity": "60%",
        "Wind Speed": "5 m/s"
    },
    "New York": {
        "Temperature": "22°C",
        "Weather": "Sunny",
        "Humidity": "55%",
        "Wind Speed": "3 m/s"
    }
}

st.title("Weather Program (Without API)")

city = st.selectbox("Select a city", list(weather_data.keys()))

if st.button("Get Weather"):
    if city in weather_data:
        weather_info = weather_data[city]
        for key, value in weather_info.items():
            st.write(f"**{key}:** {value}")
    else:
        st.write("City not found in the hardcoded data.")
