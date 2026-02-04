import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city: str):
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    return {
        "city": city,
        "temperature_celsius": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }
