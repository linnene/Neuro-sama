from contextlib import asynccontextmanager
from fastapi import FastAPI
from neuro_sama.core.database import create_db_and_tables
from neuro_sama.api.routes import dialogue

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(dialogue.router, prefix="/dialogues", tags=["dialogues"])
