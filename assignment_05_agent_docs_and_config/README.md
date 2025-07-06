# 📘 Assignment 5: Deep Dive into Agents SDK

## 🎯 Objective

This assignment focuses on understanding the core architecture of OpenAI's `agents-python` SDK — including how agents, tools, configurations, and model settings are structured and integrated.

Rather than building something hands-on, this task is about studying the foundation needed to develop production-grade agentic applications.

---

## 📚 Learning Scope

You are expected to thoroughly read and understand the following official OpenAI Agent SDK documentation:

| 📄 Section | 🔗 Link |
|-----------|--------|
| 🔹 Agents Overview | [Agents Docs](https://openai.github.io/openai-agents-python/agents/) |
| 🔹 Tools Overview | [Tools Docs](https://openai.github.io/openai-agents-python/tools/) |
| 🔹 Full Reference Docs | [SDK Reference](https://openai.github.io/openai-agents-python/ref/) |
| 🔹 Agent Class Reference | [Agent Class](https://openai.github.io/openai-agents-python/ref/agent/) |
| 🔹 Model Settings Reference | [ModelSettings](https://openai.github.io/openai-agents-python/ref/model_settings/#agents.model_settings.ModelSettings) |

---

## 🧠 Key Takeaways

### 1. 🧠 **Agent Fundamentals**
- An `Agent` represents a reasoning engine with memory, tools, and model configuration.
- It receives user input, decides whether a tool is needed, and returns a final response.
- It can operate in multi-step workflows (`runs`) within `threads`.

### 2. 🛠 **Tool Integration**
- A `Tool` is a Python function with a name, description, and schema.
- Agents can automatically decide when and how to invoke tools using semantic reasoning.
- Tools must be registered using decorators or explicitly declared in the `Agent` instance.

### 3. ⚙️ **Configuration Layers**
| Level | Description |
|-------|-------------|
| **Global Config** | Affects all agents by default |
| **Agent Config** | Overrides default for a specific agent |
| **Run Config** | Temporary, used per-execution basis (for overrides/testing) |

Model behavior (like temperature, max tokens, etc.) can be fine-tuned via `ModelSettings`.

### 4. 💡 **RunConfig & Execution Flow**
- `RunConfig` lets you customize how a particular agent run behaves (model switch, system prompt, etc.)
- A `Run` is a specific execution inside a `Thread`.
- Each thread maintains state/context, making multi-turn conversations possible.

---

## 🛠 Key Components to Explore in Code (Later Assignments)

- `Agent` Class
- `Tool` Decorator or Class
- `RunConfig`, `ModelSettings`
- `Thread`, `Run`, `Message` APIs
- Tool I/O schema definitions

---

## 🧑‍💻 Use Cases You’ll Be Able to Build After This

- 🧮 Agents that call custom tools like calculators, APIs, or databases
- 🧭 Context-aware multi-turn chat assistants with memory
- 📈 Configurable agents that behave differently for different business scenarios
- 🧩 Modular toolchains for chaining logic and decisions

---

## ✅ Deliverable

- This `README.md` acts as your submission for Assignment 5.
- Optionally, include:
  - 📝 Notes on each link you explored
  - 📸 Screenshots of diagrams or highlights you liked
  - ❓ Questions or doubts you noted while reading

---

## 🔗 Pro Tip

> ⭐ You’ll use this understanding in upcoming real-world agent projects, where tool orchestration, context management, and agent decision logic are critical.

---

## 🙌 Conclusion

This assignment isn’t about output — it’s about **input**. By studying these docs, you’ve taken a big leap toward becoming an **Agentic AI Developer** — someone who builds smart, composable, reasoning-based apps with OpenAI’s evolving SDK.

Keep going, keep showing up. The real magic is just beginning. 🚀

---

