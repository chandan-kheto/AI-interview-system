
from backend.services.llm_service import generate_questions
from backend.routes.resume_routes import router as resume_router
from backend.routes.interview_routes import router as interview_router
from backend.routes.answer_routes import router as answer_router
from backend.routes.evaluation_routes import router as evaluation_router
from fastapi.middleware.cors import CORSMiddleware

from backend.database.db import engine
from backend.models.interview_model import Base

from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)


# Register routes
app.include_router(resume_router)
app.include_router(interview_router)
app.include_router(answer_router)
app.include_router(evaluation_router)


@app.get("/")
def home():
    return {"message": "AI Interview System Running"}

@app.get("/test-llm")
def test_llm():

    response = generate_questions(
        "Generate 2 machine learning interview questions"
    )

    return {"response": response}

