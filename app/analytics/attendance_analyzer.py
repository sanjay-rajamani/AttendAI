from sqlalchemy.orm import Session

from app.models.subject import Subject
from app.models.attendance import Attendance


def calculate_subject_percentage(db: Session, subject_id: int):

    total = (
        db.query(Attendance)
        .filter(
            Attendance.subject_id == subject_id
        )
        .count()
    )

    present = (
        db.query(Attendance)
        .filter(
            Attendance.subject_id == subject_id,
            Attendance.status == "Present"
        )
        .count()
    )

    if total == 0:
        percentage = 0.0
    else:
        percentage = round((present / total) * 100, 2)

    # ------------------------
    # Attendance Alert
    # ------------------------

    if percentage < 75:
        alert = "🚨 Critical - Attendance below 75%"

    elif percentage < 80:
        alert = "⚠ Warning - Attendance below 80%"

    else:
        alert = "✅ Safe"

    subject = (
        db.query(Subject)
        .filter(
            Subject.id == subject_id
        )
        .first()
    )

    return {
        "subject_id": subject.id,
        "subject_name": subject.subject_name,
        "subject_code": subject.subject_code,
        "present": present,
        "total": total,
        "percentage": percentage,
        "alert": alert
    }