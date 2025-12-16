from datetime import datetime
from pydantic import BaseModel

class Dialogue(BaseModel):
    """
    Represents a single Q&A interaction or dialogue turn.
    """
    dialogue_id: str
    stream_id: str
    question: str
    answer: str
    timestamp: datetime
    speaker: str | None = None
    confidence: float | None = None
