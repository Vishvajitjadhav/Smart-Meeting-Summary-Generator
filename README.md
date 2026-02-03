# 🧠 Smart Meeting Summary Generator

A prototype application that converts raw meeting notes into **structured, actionable summaries** including topics discussed, key decisions, and action items.

This project was built as part of an **AI technical assessment** to demonstrate real-world AI integration, clean architecture, and robust handling of LLM variability.

---

## ✨ Features

- Paste raw meeting notes and generate:
  - Topics discussed
  - Key decisions
  - Action items (task, owner, due date)
- Simple and intuitive UI using **Streamlit**
- Uses a **real LLM (Groq – LLaMA 3.1)** for fast inference
- Strong focus on:
  - Structured output
  - Schema validation
  - Hallucination management
- Modular and **LLM-agnostic** design

---

## 📁 Project Structure

```text
Smart-Meeting-Summary/
├── app.py                     # Streamlit UI entry point
│
├── services/                  # Business logic & integrations
│   ├── summarizer.py          # LLM interaction + normalization
│   └── prompt_builder.py      # Prompt construction
│
├── models/                    # Data contracts & validation
│   └── summary_schema.py      # Pydantic schema
│
├── requirements.txt           # Project dependencies
├── README.md                  # Documentation
│
└── venv/                      # Local virtual environment

```

### Why this structure?
- Clear separation of concerns (UI, AI logic, data contracts)
- Easy to test and maintain
- LLM provider can be swapped with minimal changes
- Mirrors real-world backend service architecture

---

## 🏗️ Architecture Overview
```text
UI (Streamlit)
↓
Prompt Builder
↓
LLM Service (Groq – LLaMA 3.1)
↓
Output Normalization
↓
Schema Validation (Pydantic)
↓
Structured Summary
```

### Key Design Decisions
- **Schema-first approach**: Output is validated using Pydantic models
- **Normalization layer**: Handles minor variations in LLM responses
- **Low temperature prompts**: Improves determinism
- **LLM abstraction**: Keeps the system provider-independent

---

## 🧪 Hallucination Management

This prototype explicitly avoids hallucinated data by:

- Enforcing **exact JSON keys** via prompt instructions
- Extracting only valid JSON from LLM responses
- Normalizing fields before validation
- Rejecting invalid or incomplete structured output

This makes the system **safe, predictable, and explainable**.

---

## 🚀 Tech Stack

- **Python**
- **Streamlit** – UI
- **Groq API** – LLaMA-3.1-8B-Instant
- **Pydantic** – Schema validation
- **Modular service-based architecture**

---

## ▶️ Demo Video

🎥 Short demo video (30–40 seconds) showing:
- Pasting meeting notes
- Generating a summary
- Reviewing structured output

**https://drive.google.com/file/d/1oR49mSGh14Pw9WiO8HKk94mN1JtoJ0oj/view?usp=sharing**  

---
## ⚙️ Running the Project Locally

### Prerequisites
- Python 3.10+
- Groq API key

### Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

(Set Environment Variable)
setx GROQ_API_KEY "your_groq_api_key"

(Restart the terminal after setting the key.)

(Run the App)
python -m streamlit run app.py

---

🔄 LLM Flexibility

The system is LLM-agnostic.

To switch providers (Gemini, OpenAI, local LLM, etc.), only
services/summarizer.py needs to be updated.

This makes the solution adaptable for enterprise environments.

---

🔮 Future Enhancements

Retrieval-Augmented Generation (RAG) using meeting history

Audio transcription (speech → text → summary)

Export summaries to PDF or task management tools

User feedback loop for improving summary quality

---

📝 Notes on Implementation Choices

Multiple LLM providers were evaluated during development.
For this prototype, Groq was selected to ensure:

Fast and reliable inference

No quota or billing blockers during evaluation

Smooth demo experience

The architecture remains production-oriented and extensible.

---
👤 Author

Vishvajit Jadhav
Software Engineer