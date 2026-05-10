
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from models.interview_model import InterviewSession

from services.llm_service import generate_questions


router = APIRouter()


@router.get("/evaluate/{session_id}")
def evaluate_interview(
    session_id: int,
    db: Session = Depends(get_db)
):

    session = db.query(InterviewSession).filter(
        InterviewSession.id == session_id
    ).first()

    if not session:

        return {
            "error": "Session not found"
        }

    prompt = f"""
    Evaluate the following technical interview.

    Role:
    {session.role}

    Candidate Skills:
    {session.skills}

    Interview Questions:
    {session.questions}

    Candidate Answers:
    {session.answers}

    Provide:
    1. Overall Performance
    2. Technical Strengths
    3. Weaknesses
    4. Hiring Recommendation
    """

    evaluation = generate_questions(prompt)

    return {
        "session_id": session.id,
        "evaluation": evaluation
    }