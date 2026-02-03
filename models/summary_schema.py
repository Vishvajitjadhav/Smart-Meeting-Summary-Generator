# Prevents Hallucination

from pydantic import BaseModel
from typing import List, Optional

class ActionItem(BaseModel):
    task: str
    owner: Optional[str]
    due_date: Optional[str]

class MeetingSummary(BaseModel):
    topics: List[str]
    decisions: List[str]
    action_items: List[ActionItem]
