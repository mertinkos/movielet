from sqlalchemy import text
from fastapi import FastAPI
from app.database.database import engine, Base
from app.database import models

with engine.connect() as conn:
    conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
    conn.commit()

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}
