from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.temporary_change import (
    TemporaryChangeCreate,
    TemporaryChangeResponse
)

from app.services.temporary_change_service import (
    create_temporary_change,
    get_all_changes
)

router = APIRouter(
    prefix="/temporary-changes",
    tags=["Temporary Changes"]
)


@router.post("/", response_model=TemporaryChangeResponse)
def add_change(
    data: TemporaryChangeCreate,
    db: Session = Depends(get_db)
):
    return create_temporary_change(db, data)


@router.get("/", response_model=list[TemporaryChangeResponse])
def view_changes(
    db: Session = Depends(get_db)
):
    return get_all_changes(db)