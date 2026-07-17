from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.subject import Subject
from app.schemas.subject import SubjectCreate, SubjectUpdate


def create_subject(db: Session, subject: SubjectCreate):

    existing = db.query(Subject).filter(
        Subject.subject_code == subject.subject_code
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Subject code already exists."
        )

    new_subject = Subject(
        subject_code=subject.subject_code,
        subject_name=subject.subject_name,
        faculty=subject.faculty
    )

    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)

    return new_subject


def get_all_subjects(db: Session):
    return db.query(Subject).all()


def get_subject(db: Session, subject_id: int):

    subject = db.query(Subject).filter(
        Subject.id == subject_id
    ).first()

    if not subject:
        raise HTTPException(
            status_code=404,
            detail="Subject not found."
        )

    return subject


def update_subject(
    db: Session,
    subject_id: int,
    data: SubjectUpdate
):

    subject = get_subject(db, subject_id)

    subject.subject_name = data.subject_name
    subject.faculty = data.faculty

    db.commit()
    db.refresh(subject)

    return subject


def delete_subject(
    db: Session,
    subject_id: int
):

    subject = get_subject(db, subject_id)

    db.delete(subject)
    db.commit()

    return {
        "message": "Subject deleted successfully."
    }