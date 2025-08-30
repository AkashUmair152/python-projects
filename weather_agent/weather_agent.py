from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner,set_tracing_disabled
from dotenv import load_dotenv
from tools import get_weather
import os
import asyncio

load_dotenv()
set_tracing_disabled(True)  # Disable tracing for simplicity

API_KEY = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=API_KEY,
)

# Fix the typo in your model name: "menini" → "gemini"
model = OpenAIChatCompletionsModel(
    openai_client=provider,
    model="gemini-2.0-flash"   # ✅ correct Gemini model
)

# Agent setup (no description arg)
weather_agent = Agent(
    name="WeatherAgent",
    model=model,
    instructions="You are a helpful assistant that can answer general knowledge and weather questions.",
    tools=[get_weather]
)



