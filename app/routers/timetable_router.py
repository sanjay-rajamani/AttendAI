from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.timetable import (
    TimetableCreate,
    TimetableResponse,
    WeeklyTimetable
)

from app.services.timetable_service import (
    add_timetable_entry,
    get_timetable,
    upload_weekly_timetable
)

router = APIRouter(
    prefix="/timetable",
    tags=["Timetable"]
)


# Create Single Timetable Entry
@router.post("/", response_model=TimetableResponse)
def create_entry(
    timetable: TimetableCreate,
    db: Session = Depends(get_db)
):
    return add_timetable_entry(db, timetable)


# View Timetable
@router.get("/", response_model=list[TimetableResponse])
def view_timetable(
    db: Session = Depends(get_db)
):
    return get_timetable(db)


# Upload Weekly Timetable
@router.post("/weekly")
def upload_week(
    timetable: WeeklyTimetable,
    db: Session = Depends(get_db)
):
    return upload_weekly_timetable(db, timetable)