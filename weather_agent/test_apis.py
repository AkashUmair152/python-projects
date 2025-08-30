# test_apis.py
import requests
from dotenv import load_dotenv
import os

load_dotenv()

weather_key = os.getenv("WEATHER_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

print("Testing WeatherAPI...")
resp = requests.get(f"http://api.weatherapi.com/v1/current.json?key={weather_key}&q=London")
print(resp.json())

print("Gemini API Key loaded:", bool(gemini_key))