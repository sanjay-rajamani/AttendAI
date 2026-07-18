from fastapi import APIRouter

from app.schemas.ai import AIRequest
from app.ai.executor import execute_command

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post("/chat")
def chat(request: AIRequest):

    return execute_command(request.message)