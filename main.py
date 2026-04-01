from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from utils.db_helper import connect_to_db as get_db

app = FastAPI()

@app.get("/")
def healt_check():
    return {"message": "Hello World!"}

@app.get("/hello")
def say_hello(name: str):
    return {"message": f"Hello {name}!"}

@app.get("/db-check")
async def db_check(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    return {"database": "connected", "result": result.scalar()}