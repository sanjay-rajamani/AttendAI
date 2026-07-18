from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.timetable import Timetable
from app.schemas.timetable import TimetableCreate


# -----------------------------
# Add Single Timetable Entry
# -----------------------------
def add_timetable_entry(db: Session, data: TimetableCreate):

    existing = (
        db.query(Timetable)
        .filter(
            Timetable.day == data.day,
            Timetable.period == data.period
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail=f"{data.day} Period {data.period} already exists."
        )

    entry = Timetable(
        day=data.day,
        period=data.period,
        subject_id=data.subject_id,
        room=data.room
    )

    db.add(entry)
    db.commit()
    db.refresh(entry)

    return entry


# -----------------------------
# View Timetable
# -----------------------------
def get_timetable(db: Session):

    return (
        db.query(Timetable)
        .order_by(
            Timetable.day,
            Timetable.period
        )
        .all()
    )


# -----------------------------
# Upload Weekly Timetable
# -----------------------------
def upload_weekly_timetable(db: Session, timetable):

    # Remove old timetable
    db.query(Timetable).delete()
    db.commit()

    # Add new timetable
    for day, periods in timetable.model_dump().items():

        for p in periods:

            entry = Timetable(
                day=day,
                period=p["period"],
                subject_id=p["subject_id"],
                room=p.get("room")
            )

            db.add(entry)

    db.commit()

    return {
        "message": "Weekly timetable uploaded successfully."
    }