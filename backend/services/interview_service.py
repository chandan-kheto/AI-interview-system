
from utils.skill_extractor import extract_skills
from rag.retriever import retrieve_context
from services.llm_service import generate_questions


def generate_interview_questions(resume_text, role):

    # Extract skills
    skills = extract_skills(resume_text)

    # Create semantic query
    query = f"""
    Generate interview questions for a {role}.
    Candidate skills: {', '.join(skills)}
    """

    # Retrieve context from vector DB
    retrieved_chunks = retrieve_context(query)

    # Combine retrieved context
    context = "\n".join(retrieved_chunks)

    # Final LLM Prompt
    final_prompt = f"""
    You are an expert technical interviewer.

    Candidate Role:
    {role}

    Candidate Skills:
    {', '.join(skills)}

    Retrieved Knowledge Context:
    {context}

    Generate 5 technical interview questions.

  Requirements:
  - Questions must be role-specific
  - Questions should match candidate background
  - Include conceptual and practical questions
  - Avoid generic questions
  - DO NOT provide answers
  - DO NOT provide explanations
  - Only return interview questions
    """

    # Generate questions
    response = generate_questions(final_prompt)

    return {
        "skills": skills,
        "questions": response
    }