from datetime import date
from sqlalchemy.orm import Session

from app.models.subject import Subject
from app.models.timetable import Timetable
from app.models.temporary_change import TemporaryChange


def get_weekly_subject(
    db: Session,
    day: str,
    period: int
):
    """
    Returns the scheduled subject for the given day and period.
    """

    entry = (
        db.query(Timetable)
        .filter(
            Timetable.day == day,
            Timetable.period == period
        )
        .first()
    )

    if entry is None:
        return None

    subject = (
        db.query(Subject)
        .filter(Subject.id == entry.subject_id)
        .first()
    )

    return subject


def get_temporary_change(
    db: Session,
    target_date: str,
    period: int
):
    """
    Returns the temporary change for the given date and period.
    """

    change = (
        db.query(TemporaryChange)
        .filter(
            TemporaryChange.date == target_date,
            TemporaryChange.period == period
        )
        .first()
    )

    return change


def resolve_schedule(
    db: Session,
    target_date: date,
    period: int
):
    """
    Returns the final subject after applying temporary changes.
    """

    day = target_date.strftime("%A")

    # Check for a temporary change first
    change = get_temporary_change(
        db,
        str(target_date),
        period
    )

    if change:

        subject = (
            db.query(Subject)
            .filter(
                Subject.id == change.subject_id
            )
            .first()
        )

        if subject:

            return {
                "source": "temporary_change",
                "subject": subject
            }

    # Otherwise use the weekly timetable
    subject = get_weekly_subject(
        db,
        day,
        period
    )

    if subject:

        return {
            "source": "weekly_timetable",
            "subject": subject
        }

    return None