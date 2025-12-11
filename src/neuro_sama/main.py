from contextlib import asynccontextmanager
from fastapi import FastAPI
from neuro_sama.core.database import create_db_and_tables
from neuro_sama.api.routes import dialogue, stream

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Neuro-sama backend is running"}

app.include_router(stream.router, prefix="/streams", tags=["streams"])
app.include_router(dialogue.router, prefix="/dialogues", tags=["dialogues"])
