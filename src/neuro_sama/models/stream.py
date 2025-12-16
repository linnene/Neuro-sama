from datetime import datetime
from pydantic import BaseModel

class Stream(BaseModel):
    """
    Represents a live stream session.
    """
    stream_id: str
    title: str
    streamer: str
    start_time: datetime
    end_time: datetime | None = None
    url: str | None = None
