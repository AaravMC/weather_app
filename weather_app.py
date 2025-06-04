import streamlit as st
from datetime import datetime
import pytz

# Full city data with 30 cities
city_data = {
    "Saratoga 🌳 (USA)": {"country": "USA", "population": "31,000", "timezone": "America/Los_Angeles", "weather": "☀️", "temp_c": 22},
    "New York 🗽 (USA)": {"country": "USA", "population": "8.8 million", "timezone": "America/New_York", "weather": "☁️", "temp_c": 18},
    "London 🎡 (UK)": {"country": "UK", "population": "9.5 million", "timezone": "Europe/London", "weather": "🌧", "temp_c": 15},
    "Tokyo 🏮 (Japan)": {"country": "Japan", "population": "14 million", "timezone": "Asia/Tokyo", "weather": "🌤", "temp_c": 24},
    "Paris 🗼 (France)": {"country": "France", "population": "11 million", "timezone": "Europe/Paris", "weather": "☀️", "temp_c": 20},
    "Delhi 🕌 (India)": {"country": "India", "population": "32 million", "timezone": "Asia/Kolkata", "weather": "🌞", "temp_c": 35},
    "San Francisco 🌁 (USA)": {"country": "USA", "population": "815,000", "timezone": "America/Los_Angeles", "weather": "🌁", "temp_c": 17},
    "Dubai 🏙️ (UAE)": {"country": "UAE", "population": "3.6 million", "timezone": "Asia/Dubai", "weather": "☀️", "temp_c": 38},
    "Cairo 🐫 (Egypt)": {"country": "Egypt", "population": "10 million", "timezone": "Africa/Cairo", "weather": "☀️", "temp_c": 30},
    "Moscow 🧊 (Russia)": {"country": "Russia", "population": "12.5 million", "timezone": "Europe/Moscow", "weather": "❄️", "temp_c": -2},
    "Toronto 🍁 (Canada)": {"country": "Canada", "population": "6.3 million", "timezone": "America/Toronto", "weather": "🌧", "temp_c": 10},
    "Rome 🏛️ (Italy)": {"country": "Italy", "population": "2.8 million", "timezone": "Europe/Rome", "weather": "🌤", "temp_c": 19},
    "Istanbul 🕌 (Turkey)": {"country": "Turkey", "population": "15 million", "timezone": "Europe/Istanbul", "weather": "🌧", "temp_c": 16},
    "Bangkok 🛕 (Thailand)": {"country": "Thailand", "population": "10.7 million", "timezone": "Asia/Bangkok", "weather": "🌩", "temp_c": 33},
    "Berlin 🏰 (Germany)": {"country": "Germany", "population": "3.6 million", "timezone": "Europe/Berlin", "weather": "🌦", "temp_c": 14},
    "Sydney 🐨 (Australia)": {"country": "Australia", "population": "5.3 million", "timezone": "Australia/Sydney", "weather": "🌤", "temp_c": 21},
    "Singapore 🏙️ (Singapore)": {"country": "Singapore", "population": "5.9 million", "timezone": "Asia/Singapore", "weather": "🌦", "temp_c": 29},
    "Mexico City 🌮 (Mexico)": {"country": "Mexico", "population": "22 million", "timezone": "America/Mexico_City", "weather": "⛅", "temp_c": 20},
    "Barcelona ⚽ (Spain)": {"country": "Spain", "population": "5.6 million", "timezone": "Europe/Madrid", "weather": "☀️", "temp_c": 22},
    "Buenos Aires 💃 (Argentina)": {"country": "Argentina", "population": "15.5 million", "timezone": "America/Argentina/Buenos_Aires", "weather": "🌤", "temp_c": 23},
    "Sao Paulo 🥁 (Brazil)": {"country": "Brazil", "population": "22 million", "timezone": "America/Sao_Paulo", "weather": "🌧", "temp_c": 26},
    "Mumbai 🎥 (India)": {"country": "India", "population": "20 million", "timezone": "Asia/Kolkata", "weather": "🌧", "temp_c": 31},
    "Chicago 🌆 (USA)": {"country": "USA", "population": "2.7 million", "timezone": "America/Chicago", "weather": "🌬", "temp_c": 12},
    "Seoul 🎶 (South Korea)": {"country": "South Korea", "population": "9.7 million", "timezone": "Asia/Seoul", "weather": "🌤", "temp_c": 19},
    "Jakarta 🏝️ (Indonesia)": {"country": "Indonesia", "population": "10.5 million", "timezone": "Asia/Jakarta", "weather": "🌧", "temp_c": 30},
    "Hong Kong 🌉 (China)": {"country": "China", "population": "7.5 million", "timezone": "Asia/Hong_Kong", "weather": "🌦", "temp_c": 27},
    "Santiago 🏔️ (Chile)": {"country": "Chile", "population": "7.1 million", "timezone": "America/Santiago", "weather": "🌤", "temp_c": 21},
    "Kuala Lumpur 🌴 (Malaysia)": {"country": "Malaysia", "population": "1.8 million", "timezone": "Asia/Kuala_Lumpur", "weather": "🌧", "temp_c": 29},
    "Lagos 🏙️ (Nigeria)": {"country": "Nigeria", "population": "21 million", "timezone": "Africa/Lagos", "weather": "⛅", "temp_c": 30},
    "Nairobi 🐘 (Kenya)": {"country": "Kenya", "population": "4.4 million", "timezone": "Africa/Nairobi", "weather": "🌦", "temp_c": 23}
}

# --- Streamlit UI ---
st.set_page_config(page_title="🌍 City Weather App", layout="centered")
st.title("🌐 World Weather Dashboard")

# Theme + unit selectors
bg_color = st.sidebar.radio("Choose a Background Theme:", ["Light Blue", "Light Red", "Light Green", "Light Yellow"])
unit = st.sidebar.radio("Choose Temperature Unit:", ["C", "F"])
colors = {
    "Light Blue": "#dbeafe",
    "Light Red": "#fdecea",
    "Light Green": "#e7fce9",
    "Light Yellow": "#fff9db"
}
st.markdown(f"<style>body {{ background-color: {colors[bg_color]}; }}</style>", unsafe_allow_html=True)

# City selection (with unique key)
selected_city = st.selectbox("Select a city:", list(city_data.keys()), key="city_selector")
info = city_data[selected_city]

# Time and temperature conversion
local_tz = pytz.timezone(info["timezone"])
local_time = datetime.now(local_tz).strftime("%Y-%m-%d %H:%M:%S")
temp_c = info["temp_c"]
temperature = temp_c if unit == "C" else round((temp_c * 9 / 5) + 32, 1)

# Display card
st.markdown("---")
st.markdown(f"### {selected_city}")
st.markdown(f"**Country:** {info['country']}")
st.markdown(f"**Population:** {info['population']}")
st.markdown(f"**Local Time:** {local_time}")
st.markdown(f"**Weather:** {info['weather']}")
st.markdown(f"**Temperature:** {temperature} °{unit}")

# City image
img_url = "https://scontent-sjc3-1.xx.fbcdn.net/v/t39.30808-6/324559494_3356789117937588_8292850894080733994_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=PvaBzsVhEskQ7kNvwFUSe_Z&_nc_oc=AdkVVQu5NhvX4_7LLeFrwYPmgqeoLWBHjJZfytDlvqzI_QzX9aEPC5doRWwHeNRCMrwwN72J7jjTQZUhRNIjmSIo&_nc_zt=23&_nc_ht=scontent-sjc3-1.xx&_nc_gid=Uj-rBuTix3n5uBsXuqWQtQ&oh=00_AfKOCH8ai37cyKFFY1xQCr9cDS9kPMJvpsDozkgoHZW5kQ&oe=6845A6BC"
st.image(img_url, caption="🌆 City View", use_container_width=True)
