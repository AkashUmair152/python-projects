from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner,set_tracing_disabled
from dotenv import load_dotenv
from tools import get_weather
import os
import asyncio

load_dotenv()
set_tracing_disabled(True)  # Disable tracing for simplicity

API_KEY = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  # ✅ no trailing space
    api_key=API_KEY,
)

# Fix the typo in your model name: "menini" → "gemini"
model = OpenAIChatCompletionsModel(
    openai_client=provider,
    model="gemini-1.5-flash"   # ✅ correct model name
)

# Agent setup (no description arg)
weather_agent = Agent(
    name="WeatherAgent",
    model=model,
    instructions=(
    "You are a helpful weather assistant. "
    "Whenever the user asks about the weather, you MUST use the `get_weather` tool. "
    "Do NOT say the tools cannot provide information. "
    "Do NOT make up excuses. "
    "Call the function and return the result exactly as given."
),
    tools=[get_weather]
)

