def build_prompt(meeting_text: str) -> str:
    return f"""
You are an AI that extracts structured information from meeting notes.

CRITICAL RULES:
- You MUST return ONLY valid JSON.
- You MUST use EXACTLY the keys defined below.
- Do NOT rename keys.
- Do NOT omit keys.
- If information is missing, use empty arrays or null values.

JSON SCHEMA (follow exactly):
{{
  "topics": [],
  "decisions": [],
  "action_items": [
    {{
      "task": "",
      "owner": null,
      "due_date": null
    }}
  ]
}}

Meeting Notes:
{meeting_text}
"""
