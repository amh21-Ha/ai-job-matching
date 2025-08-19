from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from resume_match.matcher import ResumeMatcher
from interview_ai.answer_eval import AnswerEvaluator
import os

app = FastAPI()

# Path to the favicon.ico file
favicon_path = os.path.join(os.path.dirname(__file__), "static", "favicon.ico")

# Mount the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

matcher = ResumeMatcher()
evaluator = AnswerEvaluator()

@app.get("/match/")
def match(job: str, resume: str):
    score = matcher.match(job, resume)
    return {"match_score": score}

@app.post("/evaluate/")
def evaluate(question: str, answer: str):
    result = evaluator.score_answer(question, answer)
    return result

