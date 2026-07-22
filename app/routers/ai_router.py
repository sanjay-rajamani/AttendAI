from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.ai import AIRequest
from app.services.ai_service import process_ai_message

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post("/chat")
def chat(
    request: AIRequest,
    db: Session = Depends(get_db)
):
    return process_ai_message(
        db=db,
        message=request.message
    )