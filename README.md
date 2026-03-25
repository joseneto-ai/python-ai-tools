# 🐍 Python AI Tools — zNeto.AI

Practical Python utilities built for real AI automation workflows.
These scripts are used internally at zNeto.AI as building blocks
for larger automation pipelines — extracted, sanitized, and documented
for reuse.

Each tool is self-contained, dependency-light, and built to plug
directly into n8n workflows, APIs, or standalone automation scripts.

---

## 🧰 Available Tools

### 1. 🧠 Message Classifier
Classifies any text input by intent using the OpenAI API.
Returns a structured JSON result ready for downstream routing logic.

→ [`/message-classifier`](./message-classifier/README.md)

---

### 2. 🔗 Webhook Payload Parser
Normalizes incoming webhook payloads from any source into a
clean, consistent data structure — regardless of origin format.

→ [`/webhook-parser`](./webhook-parser/README.md)

---

### 3. 📊 Automated Report Generator
Takes raw interaction or lead data and generates a structured
summary report using an LLM — ready to send to clients or
internal teams.

→ [`/report-generator`](./report-generator/README.md)

---

## ⚙️ Requirements

- Python 3.10+
- `openai` library — `pip install openai`
- `python-dotenv` — `pip install python-dotenv`

Each tool folder contains its own setup instructions.

---

## 🔐 Environment Variables

All tools read credentials from a `.env` file.
Never hardcode API keys. A `.env.example` file is provided
in each tool folder as a reference.

---

## 👤 Author

**José Neto** — AI Automation Engineer & Founder @zNeto.AI

[![LinkedIn](https://img.shields.io/badge/LinkedIn-José%20Neto-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/jos%C3%A9-neto-b88558398)
[![GitHub](https://img.shields.io/badge/GitHub-joseneto--ai-181717?style=flat&logo=github)](https://github.com/joseneto-ai)
```
