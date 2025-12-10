from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from neuro_sama.models import Dialogue
from neuro_sama.core.database import get_session

router = APIRouter()

@router.post("/", response_model=Dialogue)
def create_dialogue(dialogue: Dialogue, session: Session = Depends(get_session)):
    session.add(dialogue)
    session.commit()
    session.refresh(dialogue)
    return dialogue

@router.get("/", response_model=list[Dialogue])
def read_dialogues(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    dialogues = session.exec(select(Dialogue).offset(offset).limit(limit)).all()
    return dialogues
