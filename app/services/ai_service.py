from datetime import date

from sqlalchemy.orm import Session

from app.ai.intent_parser import parse_intent
from app.models.subject import Subject
from app.models.attendance import Attendance

from app.schemas.attendance import AttendanceCreate

from app.services.attendance_service import mark_attendance


# ----------------------------------------------------
# AI Mark Attendance
# ----------------------------------------------------
def ai_mark_attendance(
    db: Session,
    subject_code: str,
    status: str
):
    """
    Mark attendance using the subject code.
    """

    subject = (
        db.query(Subject)
        .filter(
            Subject.subject_code.ilike(subject_code)
        )
        .first()
    )

    if subject is None:
        return {
            "success": False,
            "message": f"Subject '{subject_code}' not found."
        }

    today = date.today()

    attendance = AttendanceCreate(
        date=today,
        day=today.strftime("%A"),
        period=1,
        subject_id=subject.id,
        status=status,
        source="AI",
        remarks="Marked via AttendAI"
    )

    mark_attendance(db, attendance)

    subject.total_classes += 1

    if status.lower() == "present":
        subject.attended_classes += 1

    db.commit()

    percentage = 0

    if subject.total_classes > 0:
        percentage = (
            subject.attended_classes /
            subject.total_classes
        ) * 100

    return {
        "success": True,
        "message": "Attendance marked successfully.",
        "data": {
            "subject": subject.subject_code,
            "status": status,
            "attendance": f"{subject.attended_classes}/{subject.total_classes}",
            "percentage": round(percentage, 2)
        }
    }


# ----------------------------------------------------
# AI Show Attendance
# ----------------------------------------------------
def ai_show_attendance(db: Session):
    """
    Show attendance summary for all subjects.
    """

    subjects = db.query(Subject).all()

    if not subjects:
        return {
            "success": False,
            "message": "No subjects found."
        }

    report = []

    for subject in subjects:

        percentage = 0

        if subject.total_classes > 0:
            percentage = (
                subject.attended_classes /
                subject.total_classes
            ) * 100

        report.append(
            {
                "subject": subject.subject_code,
                "attendance": f"{subject.attended_classes}/{subject.total_classes}",
                "percentage": round(percentage, 2)
            }
        )

    return {
        "success": True,
        "message": "Attendance report",
        "data": report
    }


# ----------------------------------------------------
# AI Attendance Percentage
# ----------------------------------------------------
def ai_attendance_percentage(db: Session):
    """
    Calculate overall attendance percentage.
    """

    subjects = db.query(Subject).all()

    total = 0
    attended = 0

    for subject in subjects:
        total += subject.total_classes
        attended += subject.attended_classes

    if total == 0:
        percentage = 0
    else:
        percentage = round(
            attended / total * 100,
            2
        )

    return {
        "success": True,
        "message": "Overall attendance percentage",
        "data": {
            "attended": attended,
            "total": total,
            "percentage": percentage
        }
    }


# ----------------------------------------------------
# Process AI Message
# ----------------------------------------------------
def process_ai_message(
    db: Session,
    message: str
):
    """
    Main AI entry point.
    """

    intent = parse_intent(message)

    action = intent.get("intent")

    # -----------------------------
    # Mark Attendance
    # -----------------------------
    if action == "mark_attendance":

        return ai_mark_attendance(
            db=db,
            subject_code=intent.get("subject", ""),
            status=intent.get("status", "Present")
        )

    # -----------------------------
    # Show Attendance
    # -----------------------------
    elif action == "show_attendance":

        return ai_show_attendance(db)

    # -----------------------------
    # Attendance Percentage
    # -----------------------------
    elif action == "attendance_percentage":

        return ai_attendance_percentage(db)

    # -----------------------------
    # Temporary Timetable Change
    # -----------------------------
    elif action == "temporary_change":

        return {
            "success": True,
            "message": "Temporary timetable change received.",
            "data": intent
        }

    # -----------------------------
    # Gemini Error
    # -----------------------------
    elif action == "error":

        return {
            "success": False,
            "message": intent.get("message"),
            "data": intent
        }

    # -----------------------------
    # Unknown Command
    # -----------------------------
    else:

        return {
            "success": False,
            "message": "Unknown command.",
            "data": intent
        }