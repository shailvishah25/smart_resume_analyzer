import os
from dotenv import load_dotenv
from google import genai

# ✅ LOAD .env FIRST (CRITICAL)
load_dotenv("backend/.env")

# ✅ READ API KEY
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

# ✅ CREATE CLIENT AFTER KEY IS LOADED
client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_resume(resume_text: str):
    prompt = f"""
    Analyze the following resume and provide:
    1. Strengths
    2. Weaknesses
    3. Improvements

    Resume:
    {resume_text}
    """

    response = client.models.generate_content(
        model="models/gemini-2.0-flash",
        contents=prompt
    )

    return response.text
