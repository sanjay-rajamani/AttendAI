from fastapi import FastAPI

from app.core.config import settings

from app.database.database import engine
from app.database.base import Base

# ==========================================
# Import Database Models
# ==========================================
import app.models.subject
import app.models.timetable
import app.models.temporary_change
import app.models.attendance

# ==========================================
# Import Routers
# ==========================================
from app.routers.subject_router import router as subject_router
from app.routers.timetable_router import router as timetable_router
from app.routers.temporary_change_router import router as temporary_change_router
from app.routers.attendance_router import router as attendance_router
from app.routers.analytics_router import router as analytics_router
from app.routers.ai_router import router as ai_router

# ==========================================
# Create Database Tables
# ==========================================
Base.metadata.create_all(bind=engine)

# ==========================================
# Create FastAPI Application
# ==========================================
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Powered WhatsApp Attendance Assistant"
)

# ==========================================
# Register All Routers
# ==========================================
app.include_router(subject_router)
app.include_router(timetable_router)
app.include_router(temporary_change_router)
app.include_router(attendance_router)
app.include_router(analytics_router)
app.include_router(ai_router)

# ==========================================
# Home Endpoint
# ==========================================
@app.get("/")
def home():
    return {
        "project": settings.APP_NAME,
        "database": "Connected",
        "status": "Running"
    }


# ==========================================
# Health Check Endpoint
# ==========================================
@app.get("/health")
def health():
    return {
        "database": "Healthy",
        "status": "OK"
    }