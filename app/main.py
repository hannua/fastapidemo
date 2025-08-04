from fastapi import FastAPI
from app.api.router import api_router
from app.core.config import settings
from app.core.database import create_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP: create DB tables
    create_tables()
    yield
    # SHUTDOWN: (optional cleanup here)

app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

app.include_router(api_router)
