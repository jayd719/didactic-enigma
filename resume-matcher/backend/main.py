from fastapi import FastAPI
from backend.services.resume_parser import extract_resume_data
from backend.services.job_matcher import match_jobs

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Resume Matcher API"}