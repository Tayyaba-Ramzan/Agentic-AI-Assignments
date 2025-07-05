# main.py

import chainlit as cl
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# 🔐 Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 🌤️ Mock weather data
mock_weather = {
    "karachi": "Karachi is currently 33°C with a hot breeze.",
    "lahore": "Lahore is 30°C and sunny today.",
    "islamabad": "Islamabad has 28°C with light rain.",
    "new york": "New York is 25°C and cloudy.",
    "london": "London is 18°C with light drizzle."
}

# 🌦️ Tool function
def get_weather(city: str) -> str:
    city_lower = city.lower()
    return mock_weather.get(city_lower, f"Sorry, I don't have weather info for {city}.")

# 💬 Chainlit message handler
@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content.lower()

    # Tool trigger keywords
    if "weather" in user_input or "temperature" in user_input:
        # Extract city name (simple logic)
        city = None
        for c in mock_weather:
            if c in user_input:
                city = c
                break

        if city:
            answer = get_weather(city)
        else:
            answer = "Please mention a city. For example: 'What’s the weather in Lahore?'"

    else:
        # Fallback to Gemini for polite handling
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(
            f"The user said: '{user_input}'. Reply politely that this agent only provides weather info."
        )
        answer = response.text

    await cl.Message(content=answer).send()
