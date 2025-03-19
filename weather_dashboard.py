import streamlit as st
import requests

API_KEY = "4af52d0118f4491cad892935251903"

def get_weather_data(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3&aqi=no&alerts=no"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    return None

# Set page configuration
st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

# Toggle button for dark/light mode
mode = st.toggle("🌙 Toggle Dark/Light Mode")

# Apply background color based on toggle
if mode:
    bg_color =   "#0D1117"# Dark
    text_color = "#FFFFFF"
else:
    bg_color = "#FFFFFF"  # Light
    text_color = "#000000"

# Inject custom CSS
st.markdown(
    f"""
    <style>
        body {{
            background-color: {bg_color};
            color: {text_color};
        }}
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Subheader
st.title("🌤️ Real-Time Weather App")
st.subheader("Get current weather & 3-day forecast")

# User Input
city = st.text_input("Enter your city name", "Hyderabad")

if st.button("Get Weather"):
    data = get_weather_data(city)
    if data:
        st.success(f"Weather for {city}")
        current = data["current"]
        st.write(f"**Temperature:** {current['temp_c']} °C")
        st.write(f"**Condition:** {current['condition']['text']}")
        st.write(f"**Humidity:** {current['humidity']}%")
        st.write(f"**Wind:** {current['wind_kph']} km/h")

        # Forecast
        st.subheader("3-Day Forecast:")
        for day in data["forecast"]["forecastday"]:
            st.write(f"📅 Date: {day['date']}")
            st.write(f"🌡️ Max: {day['day']['maxtemp_c']}°C | Min: {day['day']['mintemp_c']}°C")
            st.write(f"🌥️ Condition: {day['day']['condition']['text']}")
            st.write("---")
    else:
        st.error("Error fetching weather data.")

# Footer
st.write("---")
st.write("Made with Python by Ameer Hamza Shah.")
