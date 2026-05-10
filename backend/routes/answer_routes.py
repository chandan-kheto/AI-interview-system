
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.dependencies import get_db
from models.interview_model import InterviewSession


router = APIRouter()


class AnswerRequest(BaseModel):

    session_id: int

    answer: str


@router.post("/submit-answer")
def submit_answer(
    data: AnswerRequest,
    db: Session = Depends(get_db)
):

    session = db.query(InterviewSession).filter(
        InterviewSession.id == data.session_id
    ).first()

    if not session:

        return {
            "error": "Session not found"
        }

    # Append answer
    current_answers = session.answers or ""

    session.answers = current_answers + "\n" + data.answer

    db.commit()

    return {
        "message": "Answer saved successfully"
    }