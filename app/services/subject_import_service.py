from sqlalchemy.orm import Session

from app.models.subject import Subject


def import_subjects(db: Session, text: str):
    """
    Import subjects from plain text.
    One subject per line.
    """

    added = 0
    skipped = 0

    for line in text.splitlines():

        subject = line.strip()

        if not subject:
            continue

        existing = (
            db.query(Subject)
            .filter(
                Subject.subject_code.ilike(subject)
            )
            .first()
        )

        if existing:
            skipped += 1
            continue

        db.add(
            Subject(
                subject_code=subject,
                subject_name=subject,
                faculty=""
            )
        )

        added += 1

    db.commit()

    return {
        "success": True,
        "message": "Subjects imported successfully.",
        "data": {
            "added": added,
            "skipped": skipped
        }
    }