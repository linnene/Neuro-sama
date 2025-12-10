from fastapi import FastAPI
from neuro_sama.core.database import create_db_and_tables
from neuro_sama.api.routes import dialogue

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(dialogue.router, prefix="/dialogues", tags=["dialogues"])
