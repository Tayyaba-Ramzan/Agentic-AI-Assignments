# main.py

import chainlit as cl
import google.generativeai as genai
import os
import re
from dotenv import load_dotenv

load_dotenv()

# 🔐 Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 🧠 Gemini Model
model = genai.GenerativeModel("gemini-pro")

# ➕ Math tool: Add function
def add(a: float, b: float) -> float:
    return a + b

# 🧠 Parse question to detect simple addition (e.g., "What is 5 + 7?")
def extract_numbers_for_addition(text):
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", text)
    if len(numbers) >= 2:
        return float(numbers[0]), float(numbers[1])
    return None, None

# 💬 Chainlit interface
@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content.lower()

    a, b = extract_numbers_for_addition(user_input)

    if "add" in user_input or "+" in user_input or "sum" in user_input:
        if a is not None and b is not None:
            result = add(a, b)
            await cl.Message(content=f"The answer is: **{result}**").send()
        else:
            await cl.Message(content="Sorry, I couldn't extract two valid numbers to add.").send()
    else:
        # fallback to Gemini for general polite response
        response = model.generate_content(
            f"User asked: '{user_input}'. Please reply politely that I only support simple math addition questions like 'What is 2 + 2'."
        )
        await cl.Message(content=response.text).send()
