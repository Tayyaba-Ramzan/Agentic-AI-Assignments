import chainlit as cl
import google.generativeai as genai
import os
import re
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

# ➕ Math Tool
def add(a: float, b: float) -> float:
    return a + b

# 🌦️ Weather Tool
def get_weather(city: str) -> str:
    return mock_weather.get(city.lower(), f"Sorry, I don't have weather info for {city}.")

# 🔍 Extract numbers from user input
def extract_numbers(text):
    return re.findall(r"[-+]?\d*\.\d+|\d+", text)

# 💬 Main Chainlit handler
@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content.lower()
    answer = ""

    # Handle math
    if any(op in user_input for op in ["+", "add", "sum"]):
        numbers = extract_numbers(user_input)
        if len(numbers) >= 2:
            result = add(float(numbers[0]), float(numbers[1]))
            answer = f"The answer is: **{result}**"
        else:
            answer = "I need two numbers to perform addition."

    # Handle weather
    elif "weather" in user_input or "temperature" in user_input:
        city = None
        for c in mock_weather:
            if c in user_input:
                city = c
                break
        if city:
            answer = get_weather(city)
        else:
            answer = "Please mention a city. Example: 'What's the weather in Karachi?'"

    # Fallback using Gemini
    else:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(
            f"The user said: '{user_input}'. Reply politely that this agent only answers math or weather questions."
        )
        answer = response.text

    await cl.Message(content=answer).send()
