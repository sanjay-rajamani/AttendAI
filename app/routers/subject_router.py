from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.subject import (
    SubjectCreate,
    SubjectUpdate,
    SubjectResponse
)

from app.services.subject_service import (
    create_subject,
    get_all_subjects,
    get_subject,
    update_subject,
    delete_subject
)

router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"]
)


@router.post("/", response_model=SubjectResponse)
def add_subject(
    subject: SubjectCreate,
    db: Session = Depends(get_db)
):
    return create_subject(db, subject)


@router.get("/", response_model=list[SubjectResponse])
def view_subjects(
    db: Session = Depends(get_db)
):
    return get_all_subjects(db)


@router.get("/{subject_id}", response_model=SubjectResponse)
def view_subject(
    subject_id: int,
    db: Session = Depends(get_db)
):
    return get_subject(db, subject_id)


@router.put("/{subject_id}", response_model=SubjectResponse)
def edit_subject(
    subject_id: int,
    subject: SubjectUpdate,
    db: Session = Depends(get_db)
):
    return update_subject(
        db,
        subject_id,
        subject
    )


@router.delete("/{subject_id}")
def remove_subject(
    subject_id: int,
    db: Session = Depends(get_db)
):
    return delete_subject(
        db,
        subject_id
    )