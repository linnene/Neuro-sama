from datetime import datetime
from pydantic import BaseModel
from typing import Literal


class QAPair(BaseModel):
    """
    已对齐的一问一答
    """
    question: Message
    answer: Message

    @classmethod
    def validate_pair(cls, question: Message, answer: Message):
        if question.role != "question":
            raise ValueError("question.role 必须是 'question'")
        if answer.role != "answer":
            raise ValueError("answer.role 必须是 'answer'")
        return cls(question=question, answer=answer)



class Message(BaseModel):
    """
    清洗后的单条消息（问 or 答）
    """
    role: Literal["question", "answer"]
    content: str
    speaker: str
    timestamp: datetime | None = None
    confidence: float | None = None

