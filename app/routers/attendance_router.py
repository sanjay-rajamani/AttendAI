from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.attendance import (
    AttendanceCreate,
    AttendanceResponse
)

from app.services.attendance_service import (
    mark_attendance,
    get_attendance
)

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("/", response_model=AttendanceResponse)
def create_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):
    return mark_attendance(db, attendance)


@router.get("/", response_model=list[AttendanceResponse])
def view_attendance(
    db: Session = Depends(get_db)
):
    return get_attendance(db)