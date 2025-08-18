from fastapi import FastAPI
from resume_match.matcher import ResumeMatcher
from interview_ai.answer_eval import AnswerEvaluator

app = FastAPI()
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

