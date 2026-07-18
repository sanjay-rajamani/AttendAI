from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate


# -----------------------------
# Mark Attendance
# -----------------------------
def mark_attendance(db: Session, data: AttendanceCreate):

    existing = (
        db.query(Attendance)
        .filter(
            Attendance.date == data.date,
            Attendance.period == data.period
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Attendance already recorded."
        )

    attendance = Attendance(
        date=data.date,
        day=data.day,
        period=data.period,
        subject_id=data.subject_id,
        status=data.status,
        source=data.source,
        remarks=data.remarks
    )

    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return attendance


# -----------------------------
# View Attendance
# -----------------------------
def get_attendance(db: Session):

    return (
        db.query(Attendance)
        .order_by(
            Attendance.date,
            Attendance.period
        )
        .all()
    )