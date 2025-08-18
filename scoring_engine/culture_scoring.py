"""
Culture Fit Scoring Module
- Evaluates candidate's text answers for cultural alignment.
- Uses simple keyword-based scoring (can be extended with embeddings/LLMs).
"""

import re
from typing import Dict

class CultureScorer:
    def __init__(self):
        # Example cultural values & keywords
        self.values = {
            "teamwork": ["team", "collaborate", "together", "support", "help"],
            "innovation": ["creative", "innovative", "ideas", "new", "improve"],
            "integrity": ["honest", "integrity", "ethics", "trust", "responsible"],
            "adaptability": ["adapt", "flexible", "change", "learn", "growth"],
            "communication": ["communicate", "explain", "clear", "listen", "share"]
        }
        self.max_score = 5  # Each category max = 5

    def preprocess(self, text: str) -> str:
        """Basic cleaning"""
        text = text.lower()
        text = re.sub(r"[^a-z\s]", "", text)
        return text

    def score_answer(self, answer: str) -> Dict[str, int]:
        """Score candidate’s cultural alignment"""
        clean_text = self.preprocess(answer)
        tokens = clean_text.split()
        scores = {}

        for value, keywords in self.values.items():
            score = sum(token in keywords for token in tokens)
            scores[value] = min(score, self.max_score)  # cap score
        return scores

    def overall_score(self, answer: str) -> float:
        """Compute normalized culture fit score"""
        scores = self.score_answer(answer)
        total = sum(scores.values())
        max_possible = len(self.values) * self.max_score
        return round((total / max_possible) * 100, 2)  # percentage

# Example usage
if __name__ == "__main__":
    scorer = CultureScorer()
    candidate_answer = """
    I strongly believe in teamwork and supporting my colleagues. 
    I always try to come up with creative solutions and adapt to challenges.
    """
    print("Detailed Scores:", scorer.score_answer(candidate_answer))
    print("Overall Culture Fit Score:", scorer.overall_score(candidate_answer), "%")

