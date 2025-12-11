from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from neuro_sama.models import Stream
from neuro_sama.core.database import get_session

router = APIRouter()

@router.post("/", response_model=Stream)
def create_stream(stream: Stream, session: Session = Depends(get_session)):
    session.add(stream)
    session.commit()
    session.refresh(stream)
    return stream

@router.get("/", response_model=list[Stream])
def read_streams(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    streams = session.exec(select(Stream).offset(offset).limit(limit)).all()
    return streams

@router.get("/{stream_id}", response_model=Stream)
def read_stream(stream_id: int, session: Session = Depends(get_session)):
    stream = session.get(Stream, stream_id)
    if not stream:
        raise HTTPException(status_code=404, detail="Stream not found")
    return stream
