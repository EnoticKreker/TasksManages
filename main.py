from fastapi import Depends, FastAPI
from pydantic import BaseModel
from typing import Annotated, Optional

from contextlib import asynccontextmanager

from data_base import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int
    name: str
    description: Optional[str] = None
    
    
tasks = []
    
@app.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"ok": True}

# @app.get("/tasks")
# def get_tasks():
#     task = Task(name="Запиши это видео")
#     return {"data": task}


