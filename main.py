from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.resume_parser import extract_text_from_pdf
from backend.llm_analyzer import analyze_resume

app = FastAPI()

# Tell FastAPI where HTML files are located
templates = Jinja2Templates(directory="frontend/templates")

# ---------------- HOME PAGE ----------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# ---------------- RESUME ANALYSIS API ----------------
@app.post("/analyze")
async def analyze(file: UploadFile):
    # Step 1: Extract text from uploaded resume PDF
    resume_text = extract_text_from_pdf(file.file)

    # Step 2: Send resume text to Gemini LLM
    analysis = analyze_resume(resume_text)

    # Step 3: Return AI response to frontend
    return {"analysis": analysis}
