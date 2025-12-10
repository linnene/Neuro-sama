from datetime import datetime
from typing import Optional, Dict, Any
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, JSON

class Dialogue(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    speaker: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    stream_id: Optional[str] = None
    # 使用 sa_column=Column(JSON) 自动处理 JSON 序列化/反序列化
    meta_info: Optional[Dict[str, Any]] = Field(default=None, sa_column=Column(JSON))
