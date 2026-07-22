from sqlalchemy.orm import Session

from app.ai.intent_parser import parse_intent
from app.services.ai_service import ai_mark_attendance


def execute_command(message: str, db: Session):
    """
    Parse the AI response and execute the requested action.
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

        return {
            "success": True,
            "message": "Attendance report requested.",
            "data": intent
        }

    # -----------------------------
    # Attendance Percentage
    # -----------------------------
    elif action == "attendance_percentage":

        return {
            "success": True,
            "message": "Attendance percentage requested.",
            "data": intent
        }

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