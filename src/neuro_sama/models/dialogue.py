from datetime import datetime
from pydantic import BaseModel
from typing import Literal



class RepeatSegment(BaseModel):
    """
    重复数据段
    维护屏幕刷屏信息
    """
    content: str
    start_time: datetime
    end_time: datetime
    count: int 

class BaseMes(BaseModel):
    """
    基础消息类
    """
    content: str
    speaker: str
    timestamp: datetime | None = None

class Message(BaseMes):
    """
    清洗后的单条消息（问 or 答）
    """
    role: Literal["que", "res"]
    confidence: float | None = None # 可选的置信度字段

class QAPair(BaseModel):
    """
    已对齐的一问一答
    """
    question: Message
    response: Message

    @classmethod
    def validate_pair(cls, question: Message, response: Message):
        if question.role != "que":
            raise ValueError("question.role 必须是 'que'")
        if response.role != "res":
            raise ValueError("response.role 必须是 'res'")
        return cls(question=question, response=response)

class MetaEvent(BaseModel):
    """
    元信息事件
    """
    pass
    #TODO: 添加元信息字段

