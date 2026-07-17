from fastapi import FastAPI

from app.core.config import settings

from app.database.database import engine
from app.database.base import Base

import app.models.subject

from app.routers.subject_router import router as subject_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Powered WhatsApp Attendance Assistant"
)

app.include_router(subject_router)


@app.get("/")
def home():

    return {
        "project": settings.APP_NAME,
        "database": "Connected",
        "status": "Running"
    }


@app.get("/health")
def health():

    return {
        "database": "Healthy",
        "status": "OK"
    }