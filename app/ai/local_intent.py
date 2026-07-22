import re


def parse_local_intent(message: str):
    """
    Parse simple attendance commands locally without using Gemini.

    Returns:
        dict -> Intent JSON
        None -> If the command is not recognized locally.
    """

    text = message.strip().lower()

    # -----------------------
    # Mark Present
    # -----------------------
    match = re.match(r"mark\s+(\w+)\s+present$", text)

    if match:
        return {
            "intent": "mark_attendance",
            "subject": match.group(1).upper(),
            "status": "Present"
        }

    match = re.match(r"(\w+)\s+present$", text)

    if match:
        return {
            "intent": "mark_attendance",
            "subject": match.group(1).upper(),
            "status": "Present"
        }

    # -----------------------
    # Mark Absent
    # -----------------------
    match = re.match(r"mark\s+(\w+)\s+absent$", text)

    if match:
        return {
            "intent": "mark_attendance",
            "subject": match.group(1).upper(),
            "status": "Absent"
        }

    match = re.match(r"(\w+)\s+absent$", text)

    if match:
        return {
            "intent": "mark_attendance",
            "subject": match.group(1).upper(),
            "status": "Absent"
        }

    # -----------------------
    # Show Attendance
    # -----------------------
    if text in [
        "show attendance",
        "attendance",
        "attendance report",
        "show my attendance"
    ]:
        return {
            "intent": "show_attendance"
        }

    # -----------------------
    # Attendance Percentage
    # -----------------------
    if text in [
        "attendance percentage",
        "percentage",
        "show percentage",
        "what is my attendance percentage"
    ]:
        return {
            "intent": "attendance_percentage"
        }

    # -----------------------
    # Help
    # -----------------------
    if text in [
        "help",
        "commands",
        "menu"
    ]:
        return {
            "intent": "help"
        }

    # -----------------------
    # Not recognized
    # -----------------------
    return None