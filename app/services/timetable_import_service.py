from sqlalchemy.orm import Session

from app.models.subject import Subject
from app.models.timetable import Timetable

from app.ai.timetable_parser import parse_timetable


def import_timetable(
    db: Session,
    timetable_text: str
):
    """
    Import an entire weekly timetable from plain text.
    """

    parsed = parse_timetable(timetable_text)

    if not parsed:
        return {
            "success": False,
            "message": "No timetable entries found."
        }

    added = 0
    updated = 0
    failed = 0
    missing_subjects = []

    for item in parsed:

        subject = (
            db.query(Subject)
            .filter(
                Subject.subject_code.ilike(item["subject"])
            )
            .first()
        )

        if subject is None:

            subject = (
                db.query(Subject)
                .filter(
                    Subject.subject_name.ilike(item["subject"])
                )
                .first()
            )

        if subject is None:

            failed += 1

            if item["subject"] not in missing_subjects:
                missing_subjects.append(item["subject"])

            continue

        timetable = (
            db.query(Timetable)
            .filter(
                Timetable.day == item["day"],
                Timetable.period == item["period"]
            )
            .first()
        )

        if timetable:

            timetable.subject_id = subject.id

            updated += 1

        else:

            timetable = Timetable(
                day=item["day"],
                period=item["period"],
                subject_id=subject.id
            )

            db.add(timetable)

            added += 1

    db.commit()

    return {
        "success": True,
        "message": "Timetable imported successfully.",
        "data": {
            "added": added,
            "updated": updated,
            "failed": failed,
            "missing_subjects": missing_subjects
        }
    }