from datetime import datetime, timezone
from typing import Optional, Dict, Any
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, JSON

if False:
    from .stream import Stream

class Dialogue(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # 外键关联到 Stream 表
    stream_id: Optional[int] = Field(default=None, foreign_key="stream.id")
    stream: Optional["Stream"] = Relationship(back_populates="dialogues")

    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    # 提问/输入 (Prompt)
    prompt_speaker: str = Field(description="提问者身份，如 'Viewer'")
    prompt_content: str = Field(description="提问内容")
    prompt_meta: Optional[Dict[str, Any]] = Field(default=None, sa_column=Column(JSON), description="提问的额外元数据")

    # 回答/输出 (Response)
    response_speaker: str = Field(description="回答者身份，如 'Neuro-sama'")
    response_content: str = Field(description="回答内容")
    response_meta: Optional[Dict[str, Any]] = Field(default=None, sa_column=Column(JSON), description="回答的额外元数据")
