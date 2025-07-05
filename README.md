# 🤖 Agentic AI Assignments (OpenAI SDK + Gemini + Chainlit)

> 🚀 A hands-on journey into building intelligent tool-using AI agents using OpenAI’s Agent SDK, Google's Gemini, and Chainlit.

---

## 🧠 What This Repo Contains

This repo showcases a complete progression of 5 foundational AI agent assignments — each one designed to build real-world, production-ready skills in **Agentic AI development**.

From static FAQs to dynamic tool-calling logic, this repo reflects not just learning — but craftsmanship. 💡

| Assignment | Description | Tech Stack |
|------------|-------------|------------|
| **1️⃣ FAQ Bot** | Static assistant that answers predefined questions | OpenAI, Chainlit |
| **2️⃣ Math Tool Agent** | Uses a registered `add()` function when triggered | Gemini, Tool Functions |
| **3️⃣ Weather Agent** | Calls a `get_weather()` function to return mocked weather | Gemini, Chainlit |
| **4️⃣ Multi-Tool Agent** | Smart agent that switches between math & weather tools | Gemini, Tool Routing |
| **5️⃣ Agent SDK Study** | Deep dive into OpenAI’s Agent SDK structure and flow | Markdown, Research |

---

## 📂 Folder Structure

```bash
Agentic-AI-Assignments/
│
├── assignment-1/         # FAQ Agent (OpenAI + Chainlit)
│   └── main.py
│   └── screenshots/
│
├── assignment-2/         # Math Tool Agent (Gemini)
│   └── main.py
│
├── assignment-3/         # Weather Tool Agent (Gemini)
│   └── main.py
│
├── assignment-4/         # Agent with Multiple Tools
│   └── main.py
│
├── assignment-5/         # Docs Study Summary
│   └── README.md
│
└── README.md             # You're here
```

## 💡 Why This Repo Matters

This repo goes beyond tutorials. It demonstrates:

- 📌 Agent decision-making with tool routing  
- 🧰 Tool registration and execution logic  
- 💬 Prompt-based triggers and natural language handling  
- ⚙️ Mock API + real SDK integration  
- 🧠 Deep understanding of OpenAI Agent SDK's flow  

---

## 🛠 Tech Stack & Tools

- 🧠 OpenAI Assistants API  
- 🧠 Google Gemini (GenerativeModel via `google.generativeai`)  
- 🧰 Chainlit for interactive UIs  
- 🧪 `dotenv` for secure key management  
- 🛜 (Optional) [weatherapi.com](https://www.weatherapi.com/) if extended to live weather  

🔐 Environment Setup
Make sure to include a .env file like:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🔍 Highlights

- ✨ Chainlit integration for real-time chat agents  
- ✨ Gemini as a fallback LLM with graceful handling  
- ✨ Tool-first design thinking  
- ✨ Clean code, modular structure  
- ✨ Dev-grade commits and repo hygiene  


## 🎓 What I Learned

- ✅ How to define and structure agents  
- ✅ How tools work behind the scenes  
- ✅ How to parse user intent  
- ✅ How to override model config using RunConfig, ModelSettings  
- ✅ Most importantly: Agent mindset > chatbot mindset  


💬 Sample Prompts to Try
| Prompt                              | Assignment        |
|-------------------------------------|-------------------|
| "What's your name?"                 | Assignment 1      |
| "What is 4 + 9?"                    | Assignment 2 & 4  |
| "Add 10 and 22"                     | Assignment 2 & 4  |
| "What’s the weather in Lahore?"    | Assignment 3 & 4  |
| "How hot is it in Karachi today?"  | Assignment 4      |

---

## 📘 Future Ideas

- 🔗 Live weather API (instead of mocked)  
- 🧠 Memory-based assistants with threading  
- 🧾 Tools that connect to DB, external APIs, LangChain  
- ✨ UI-enhanced Chainlit dashboards  

---

## 🧠 Final Thought

> I didn't just build assignments —  
> I built **agentic confidence**.  
> The future of software isn’t static.  
> It **reasons, decides, and adapts**.  
> This repo is a glimpse into that future.

---

## ⭐ If this repo inspires you...

Give it a ⭐ star  
🔁 Clone it  
🔧 Fork it  
Or build your own **agentic magic** 🧠✨

---

**#HappyCoding 👩‍💻✨**

