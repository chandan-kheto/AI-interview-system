
from fastapi import APIRouter, UploadFile, File
import os, shutil
from utils.pdf_parser import extract_text_from_pdf


router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(file_path)

    return {
        "message": "Resume uploaded successfully",
        "resume_text": resume_text
    }