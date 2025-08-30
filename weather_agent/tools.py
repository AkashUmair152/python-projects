from agents import function_tool
from dotenv import load_dotenv
import os

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@function_tool
def get_weather(location: str) -> str:
    """
    Fetches the weather for the given location using mock data.

    Args:
        location (str): The name of the location to get weather for.
    """
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}")
    if response.status_code == 200:
        data = response.json()
        return f"{data['current']['condition']['text']}, {data['current']['temp_c']}°C"
    else:
        return "Location not found"