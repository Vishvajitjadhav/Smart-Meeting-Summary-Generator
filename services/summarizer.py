import os
import json
from groq import Groq
from models.summary_schema import MeetingSummary
from services.prompt_builder import build_prompt


client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def extract_json(text: str) -> str:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("No JSON found in response")
    return text[start:end + 1]


def normalize_summary(data: dict) -> dict:
    if "topics" not in data:
        data["topics"] = data.get("topics_discussed", [])

    if "decisions" not in data:
        data["decisions"] = []

    normalized_items = []
    for item in data.get("action_items", []):
        normalized_items.append({
            "task": item.get("task") or item.get("description"),
            "owner": item.get("owner"),
            "due_date": item.get("due_date")
        })

    data["action_items"] = normalized_items
    return data


def generate_summary(meeting_text: str) -> MeetingSummary:
    prompt = build_prompt(meeting_text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Extract meeting summaries strictly in JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content
    clean_json = extract_json(content)
    data = json.loads(clean_json)

    normalized = normalize_summary(data)
    return MeetingSummary(**normalized)
