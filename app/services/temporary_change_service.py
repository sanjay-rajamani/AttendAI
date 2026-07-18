from sqlalchemy.orm import Session

from app.models.temporary_change import TemporaryChange
from app.schemas.temporary_change import TemporaryChangeCreate


def create_temporary_change(db: Session, data: TemporaryChangeCreate):

    change = TemporaryChange(
        date=data.date,
        period=data.period,
        subject_id=data.subject_id,
        faculty=data.faculty,
        reason=data.reason
    )

    db.add(change)
    db.commit()
    db.refresh(change)

    return change


def get_all_changes(db: Session):

    return db.query(TemporaryChange).all()