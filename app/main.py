from fastapi import FastAPI
from database.database import engine, Base


app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}

Base.metadata.create_all(bind = engine)