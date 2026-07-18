from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.analytics.attendance_analyzer import (
    calculate_subject_percentage
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/subject/{subject_id}")
def analyze_subject(
    subject_id: int,
    db: Session = Depends(get_db)
):
    return calculate_subject_percentage(
        db,
        subject_id
    )