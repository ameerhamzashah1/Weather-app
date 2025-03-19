import streamlit as st
import requests

# API Key
API_KEY = "4af52d0118f4491cad892935251903"

# Function to fetch weather data
def get_weather_data(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3&aqi=no&alerts=no"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    return None

# Streamlit UI Config
st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="centered")

# Dark/Light Mode Toggle
mode = st.sidebar.radio("Choose Mode", ("Light Mode", "Dark Mode"))

if mode == "Dark Mode":
    st.markdown(
        """
        <style>
        .main {
            background-color: #121212;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .main {
            background-color: white;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Title & Subheader
st.title("🌤️ Real-Time Weather Dashboard")
st.subheader("Check the current weather and 3-day forecast")

# City Input
city = st.text_input("Enter your city name", "Hyderabad")

# Get Weather Button
if st.button("Get Weather"):
    data = get_weather_data(city)
    if data:
        st.success(f"Weather details for {city}")
        # Current Weather Details
        current = data["current"]
        st.write(f"**Temperature:** {current['temp_c']} °C")
        st.write(f"**Condition:** {current['condition']['text']}")
        st.write(f"**Humidity:** {current['humidity']}%")
        st.write(f"**Wind Speed:** {current['wind_kph']} km/h")

        # 3-Day Forecast
        st.subheader("3-Day Forecast:")
        for day in data["forecast"]["forecastday"]:
            st.write(f"📅 Date: {day['date']}")
            st.write(f"🌡️ Max: {day['day']['maxtemp_c']}°C | Min: {day['day']['mintemp_c']}°C")
            st.write(f"🌥️ Condition: {day['day']['condition']['text']}")
            st.write("---")
    else:
        st.error("Unable to fetch weather data. Please try again.")

st.write("---")
st.write("Created by Ameer Hamza.")
