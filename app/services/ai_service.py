from sqlalchemy.orm import Session

from app.ai.executor import execute_command


def process_ai_message(db: Session, message: str):
    """
    Central AI service.

    All AI requests should come here before
    reaching the executor.
    """

    return execute_command(
        message=message,
        db=db
    )