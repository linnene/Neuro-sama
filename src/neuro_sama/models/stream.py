from datetime import datetime, timezone
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

if False:
    from .dialogue import Dialogue

class Stream(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    platform: str = Field(description="直播平台，如 'twitch', 'youtube'")
    channel_name: str = Field(description="直播间名称/ID，如 'vedal987'")
    stream_title: Optional[str] = Field(default=None, description="直播标题")
    started_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    # Relationship
    dialogues: List["Dialogue"] = Relationship(back_populates="stream")
