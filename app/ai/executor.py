from app.ai.intent_parser import parse_intent


def execute_command(message: str, db):
    """
    Parse the AI response and dispatch commands.
    """

    intent = parse_intent(message)

    action = intent.get("intent")

    if action == "mark_attendance":
        return {
            "success": True,
            "message": f"Attendance marked for {intent.get('subject')}",
            "data": intent
        }

    elif action == "show_attendance":
        return {
            "success": True,
            "message": "Attendance report requested.",
            "data": intent
        }

    elif action == "attendance_percentage":
        return {
            "success": True,
            "message": "Attendance percentage requested.",
            "data": intent
        }

    elif action == "temporary_change":
        return {
            "success": True,
            "message": "Temporary timetable change received.",
            "data": intent
        }

    elif action == "error":
        return {
            "success": False,
            "message": intent.get("message"),
            "data": intent
        }

    else:
        return {
            "success": False,
            "message": "Unknown command.",
            "data": intent
        }