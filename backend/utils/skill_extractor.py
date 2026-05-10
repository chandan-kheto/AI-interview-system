
def extract_skills(resume_text):

    skills_db = [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "FastAPI",
        "Flask",
        "SQL",
        "React",
        "Java",
        "Spring Boot",
        "Docker",
        "AWS",
        "NLP",
        "Pandas",
        "NumPy",
        "Scikit-learn"
    ]

    found_skills = []

    resume_lower = resume_text.lower()

    for skill in skills_db:

        if skill.lower() in resume_lower:
            found_skills.append(skill)

    return found_skills