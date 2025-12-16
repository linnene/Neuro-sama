from datetime import datetime
from pydantic import BaseModel

class Stream(BaseModel):
    """
    Represents a live stream session.
    
    stream_id: Unique identifier for the stream.
    title: Title of the stream.
    streamer: Name of the streamer.
    start_time: When the stream started.
    end_time: When the stream ended (optional).
    url: URL of the stream (optional).
    """
    stream_id: str
    title: str
    streamer: str
    start_time: datetime
    end_time: datetime | None = None
    url: str | None = None
