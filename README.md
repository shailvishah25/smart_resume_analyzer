# 🧠 Smart Resume Analyzer (GENAI Project)

Smart Resume Analyzer is a GENAI-based web application that analyzes resumes using a Large Language Model (LLM). Users can upload their resume in PDF format, and the system provides intelligent feedback such as extracted skills, resume rating, strengths, weaknesses, and improvement suggestions.

This project is developed to demonstrate practical understanding of GENAI concepts, LLM API usage, backend–frontend integration, and clean software architecture. It is suitable for internships, final-year projects, and portfolio showcasing.

---

## 🚀 Features

- Upload resume in PDF format  
- Extract text from resume  
- AI-powered resume analysis using LLM  
- Extracted skills from resume  
- Resume rating and evaluation  
- Strengths and weaknesses analysis  
- Improvement suggestions  
- Dark theme UI  
- Hover, transition, and animation effects  
- Clean and modular code structure  

---

## 🛠️ Tech Stack

Backend:
- Python
- FastAPI
- Uvicorn
- PyPDF2
- python-dotenv
- LLM API (OpenAI / Gemini / Groq)

Frontend:
- HTML
- Tailwind CSS
- JavaScript (Fetch API)

---

## 📁 Project Structure

# 🧠 Smart Resume Analyzer (GENAI Project)

Smart Resume Analyzer is a GENAI-based web application that analyzes resumes using a Large Language Model (LLM). Users can upload their resume in PDF format, and the system provides intelligent feedback such as extracted skills, resume rating, strengths, weaknesses, and improvement suggestions.

This project is developed to demonstrate practical understanding of GENAI concepts, LLM API usage, backend–frontend integration, and clean software architecture. It is suitable for internships, final-year projects, and portfolio showcasing.

---

## 🚀 Features

- Upload resume in PDF format  
- Extract text from resume  
- AI-powered resume analysis using LLM  
- Extracted skills from resume  
- Resume rating and evaluation  
- Strengths and weaknesses analysis  
- Improvement suggestions  
- Dark theme UI  
- Hover, transition, and animation effects  
- Clean and modular code structure  

---

## 🛠️ Tech Stack

Backend:
- Python
- FastAPI
- Uvicorn
- PyPDF2
- python-dotenv
- LLM API (OpenAI / Gemini / Groq)

Frontend:
- HTML
- Tailwind CSS
- JavaScript (Fetch API)

---

## 📁 Project Structure

smart-resume-analyzer/
│
├── backend/
│ ├── main.py # FastAPI entry point and API routes
│ ├── resume_parser.py # Extracts text from resume PDF
│ ├── llm_analyzer.py # Communicates with LLM API
│ ├── config.py # Loads environment variables and API key
│ ├── requirements.txt # Backend dependencies
│ └── .env # LLM API key (not pushed to GitHub)
│
├── frontend/
│ └── templates/
│ └── index.html # HTML + Tailwind CSS UI
│
└── README.md

---

## 🔄 Application Workflow

1. User opens the web application  
2. User uploads a resume PDF  
3. Frontend sends the resume file to the FastAPI backend  
4. Backend extracts text from the PDF resume  
5. Extracted text is sent to the LLM using a prompt  
6. LLM analyzes the resume and generates insights  
7. Backend returns the AI-generated analysis  
8. Frontend displays the result on the UI  

---

## 🔐 Environment Setup

Create a `.env` file inside the `backend` folder and add your LLM API key:

OPENAI_API_KEY=your_api_key_here


This file is used to securely store sensitive credentials and should never be committed to GitHub.

---

## ▶️ How to Run the Project

Clone the repository and navigate to the project directory:

```bash
git clone <your-repository-url>
cd smart-resume-analyzer

cd backend
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS/Linux
pip install -r requirements.txt

start the FastAPI server:
uvicorn main:app --reload

Open your browser and visit:
http://127.0.0.1:8000
