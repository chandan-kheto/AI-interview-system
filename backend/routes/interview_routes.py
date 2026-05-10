
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from services.interview_service import generate_interview_questions

from database.dependencies import get_db
from models.interview_model import InterviewSession


router = APIRouter()


# Request Body
class InterviewRequest(BaseModel):
    resume_text: str
    role: str


# Generate Interview Questions
@router.post("/generate-interview")
def generate_interview(
    data: InterviewRequest,
    db: Session = Depends(get_db)
):

    # Generate questions using AI pipeline
    result = generate_interview_questions(
        data.resume_text,
        data.role
    )

    # Save interview session in database
    new_session = InterviewSession(

        role=data.role,

        resume_text=data.resume_text,

        skills=", ".join(result["skills"]),

        questions=result["questions"],

        answers=""
    )

    db.add(new_session)

    db.commit()

    db.refresh(new_session)

    # Return response
    return {
        "session_id": new_session.id,
        "skills": result["skills"],
        "questions": result["questions"]
    }