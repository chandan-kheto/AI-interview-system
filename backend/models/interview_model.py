
from sqlalchemy import Column, Integer, String, Text

from database.db import Base


class InterviewSession(Base):

    __tablename__ = "interview_sessions"

    id = Column(Integer, primary_key=True, index=True)

    role = Column(String(255))

    resume_text = Column(Text)

    skills = Column(Text)

    questions = Column(Text)

    answers = Column(Text)