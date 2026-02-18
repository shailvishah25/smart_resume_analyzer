import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/.env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Gemini API key not found")
