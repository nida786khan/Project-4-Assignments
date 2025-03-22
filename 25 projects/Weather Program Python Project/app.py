# Weather Program using Streamlit and OpenWeather API
import requests
import streamlit as st

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            weather = {
                "City": data["name"],
                "Temperature": f"{data["main"]["temp"]}°C",
                "Weather": data["weather"][0]["description"].title(),
                "Humidity": f"{data["main"]["humidity"]}%",
                "Wind Speed": f"{data["wind"]["speed"]} m/s"
            }
            return weather
        else:
            return {"Error": "City not found."}
    except Exception as e:
        return {"Error": str(e)}

st.title("Weather Program")
city = st.text_input("Enter city name")

if st.button("Get Weather"):
    if city:
        weather_info = get_weather(city)
        for key, value in weather_info.items():
            st.write(f"**{key}:** {value}")
    else:
        st.write("Please enter a city name.")
