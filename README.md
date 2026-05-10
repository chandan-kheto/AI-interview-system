🤖 AI Interview System

An AI-powered mock interview platform that generates personalized technical interview questions from a candidate's resume using LLMs, RAG, and semantic search.

Built with FastAPI, React, MySQL, FAISS, and Llama 3.

```
🚀 Features
✅ Resume Upload & Parsing
Upload PDF resumes
Automatic text extraction using pdfplumber
Resume content auto-filled into frontend
✅ AI Interview Question Generation
Role-based interview generation
Personalized technical questions based on candidate skills
Powered by Llama 3 via OpenRouter API
✅ RAG (Retrieval-Augmented Generation)
Semantic retrieval using FAISS vector database
Sentence embeddings using all-MiniLM-L6-v2
Context-aware question generation
✅ AI Evaluation System
Submit candidate answers
AI-generated interview evaluation
Strengths and weaknesses analysis
Technical feedback generation
✅ Full Stack Architecture
React frontend
FastAPI backend
MySQL database integration
REST API architecture
```
🛠️ Tech Stack

Frontend: React, Tailwind CSS, Axios, Vite

Backend: FastAPI, Python, SQLAlchemy, Uvicorn, AI / ML, Llama 3, Sentence Transformers, FAISS, RAG Pipeline, all-MiniLM-L6-v2, Database, MySQL

```
📂 Project Structure
AI-interview-system/
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── database/
│   ├── vectorstore/
│   ├── knowledge_base/
│   ├── uploads/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── package.json
│
└── README.md
```

⚙️ System Workflow
Resume Upload
      ↓
PDF Parsing
      ↓
Resume Text Extraction
      ↓
FAISS Semantic Retrieval
      ↓
Llama 3 Question Generation
      ↓
Candidate Answer Submission
      ↓
AI Interview Evaluation

🧠 How RAG Works
PDFs from the knowledge base are processed
Text is chunked into smaller sections
SentenceTransformer generates embeddings
Embeddings are stored in FAISS vector database
Relevant chunks are retrieved during interview generation
Llama 3 uses retrieved context to generate better questions

📸 Screenshots
Home Page
Resume upload
Role selection
Generate interview flow
Generated Questions
AI-generated personalized interview questions
AI Evaluation
Candidate answer submission
AI-based feedback and evaluation

🔧 Backend Setup
1. Clone Repository
git clone <your-github-repo-url>
cd AI-interview-system
2. Create Virtual Environment
python -m venv venv
3. Activate Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Run Backend
uvicorn main:app --reload

Backend runs at: http://127.0.0.1:8000
💻 Frontend Setup
1. Open Frontend
cd frontend
2. Install Dependencies
npm install
3. Run Frontend
npm run dev

Frontend runs at: http://localhost:5173

🗄️ MySQL Setup
Create Database: CREATE DATABASE ai_interview_system;

Update database credentials inside:

backend/database/database.py
🔑 Environment Variables

Create a .env file inside backend:

OPENROUTER_API_KEY=your_api_key_here

📌 API Endpoints
Upload Resume
POST /upload-resume
Generate Interview
POST /generate-interview
Submit Answer
POST /submit-answer
Evaluate Interview
GET /evaluate/{session_id}
🎯 Future Improvements
Voice-based interview mode
Authentication system
Multi-user support
Cloud deployment
Interview analytics dashboard
Real-time AI interviewer
📈 Learning Outcomes

This project demonstrates:

Full-stack AI application development
Retrieval-Augmented Generation (RAG)
Vector databases using FAISS
LLM integration with APIs
Backend API development with FastAPI
MySQL database integration
Frontend-backend communication
AI-powered workflow orchestration

👨‍💻 Author
Chandan Kheto
AI/ML & Backend Developer
Python | FastAPI | React | LLM | RAG | Machine Learning
