import chainlit as cl
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# 🔐 Set Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 🧠 Configure Gemini model
model = genai.GenerativeModel("gemini-pro")

# 🎯 Define predefined FAQ responses
faq_answers = {
    "what is your name?": "I am a helpful FAQ bot created using Gemini by Google.",
    "what can you do?": "I can answer frequently asked questions in a friendly and informative way.",
    "who created you?": "I was built using the Gemini API as part of a learning project.",
    "how can I use you?": "Just type your question and I’ll try to help with a predefined answer.",
    "what is your purpose?": "My purpose is to assist users by answering common FAQ-style questions."
}

# 💬 Handle messages from user
@cl.on_message
async def handle_message(message: cl.Message):
    question = message.content.lower().strip()

    # Check if question exists in predefined set
    if question in faq_answers:
        answer = faq_answers[question]
    else:
        # Fallback: Ask Gemini to handle unexpected input politely
        response = model.generate_content(
            f"The user asked: '{question}'. Please reply politely saying that I only answer a fixed set of FAQ questions."
        )
        answer = response.text

    await cl.Message(content=answer).send()
