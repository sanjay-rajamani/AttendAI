from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.subject import SubjectCreate
from app.schemas.imports import TextImport

from app.services.subject_service import (
    create_subject,
    get_subjects
)
from app.services.subject_import_service import import_subjects

router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"]
)


# ---------------------------------
# Create Subject
# ---------------------------------
@router.post("/")
def add_subject(
    subject: SubjectCreate,
    db: Session = Depends(get_db)
):
    return create_subject(db, subject)


# ---------------------------------
# Get All Subjects
# ---------------------------------
@router.get("/")
def view_subjects(
    db: Session = Depends(get_db)
):
    return get_subjects(db)


# ---------------------------------
# Bulk Import Subjects
# ---------------------------------
@router.post("/import")
def bulk_import_subjects(
    request: TextImport,
    db: Session = Depends(get_db)
):
    return import_subjects(
        db=db,
        text=request.text
    )