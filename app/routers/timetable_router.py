from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.timetable import (
    TimetableCreate,
    WeeklyTimetable
)
from app.schemas.imports import TextImport

from app.services.timetable_service import (
    add_timetable_entry,
    get_timetable,
    upload_weekly_timetable
)
from app.services.timetable_import_service import import_timetable

router = APIRouter(
    prefix="/timetable",
    tags=["Timetable"]
)


# ---------------------------------
# Add Single Timetable Entry
# ---------------------------------
@router.post("/")
def add_timetable(
    timetable: TimetableCreate,
    db: Session = Depends(get_db)
):
    return add_timetable_entry(
        db,
        timetable
    )


# ---------------------------------
# View Timetable
# ---------------------------------
@router.get("/")
def view_timetable(
    db: Session = Depends(get_db)
):
    return get_timetable(db)


# ---------------------------------
# Upload Weekly Timetable
# ---------------------------------
@router.post("/weekly")
def upload_weekly(
    timetable: WeeklyTimetable,
    db: Session = Depends(get_db)
):
    return upload_weekly_timetable(
        db,
        timetable
    )


# ---------------------------------
# Bulk Import Timetable
# ---------------------------------
@router.post("/import")
def bulk_import_timetable(
    request: TextImport,
    db: Session = Depends(get_db)
):
    return import_timetable(
        db=db,
        timetable_text=request.text
    )