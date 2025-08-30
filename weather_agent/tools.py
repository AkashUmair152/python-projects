# tools.py
from agents import function_tool
from dotenv import load_dotenv
import os
import requests

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@function_tool
def get_weather(location: str) -> str:
    print(f"🔧 [DEBUG] get_weather tool called with location: {location}")  # 👈 ADD THIS

    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}&aqi=no"
        response = requests.get(url)

        print(f"📡 [DEBUG] API Response Status: {response.status_code}")  # 👈 SEE IF REQUEST SENT

        if response.status_code == 200:
            data = response.json()
            condition = data["current"]["condition"]["text"]
            temp_c = data["current"]["temp_c"]
            result = f"The weather in {location} is {condition}, {temp_c}°C."
            print(f"✅ [DEBUG] Success: {result}")
            return result
        else:
            error_msg = f"❌ [DEBUG] WeatherAPI error: {response.text}"
            print(error_msg)
            return f"Could not retrieve weather for {location}."
    except Exception as e:
        error_msg = f"💥 [DEBUG] Exception in get_weather: {str(e)}"
        print(error_msg)  # This will show in terminal
        return f"Error getting weather: {str(e)}"