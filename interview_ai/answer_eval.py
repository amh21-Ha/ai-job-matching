from transformers import pipeline

class AnswerEvaluator:
    def __init__(self):
        self.qa = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

    def score_answer(self, question: str, answer: str) -> dict:
        sentiment = self.qa(answer)[0]
        return {
            "question": question,
            "answer": answer,
            "score": sentiment['score'],
            "label": sentiment['label']
        }

