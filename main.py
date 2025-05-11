from fastapi import FastAPI
from contextlib import asynccontextmanager
from data_base import create_tables, delete_tables
from router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("database clear")
    await create_tables()
    print("database completed")
    yield
    print("OFF")

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)