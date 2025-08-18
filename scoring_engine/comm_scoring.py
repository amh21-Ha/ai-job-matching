"""
Communication Scoring Module
----------------------------
Evaluates communication quality from interview transcripts.

Metrics:
- Clarity: sentence length, coherence
- Conciseness: avoids long rambling
- Filler words: counts "um", "uh", "like", etc.
- Vocabulary richness: unique word ratio
"""

import re
import numpy as np

FILLER_WORDS = {"um", "uh", "like", "you know", "so", "actually", "basically"}

class CommunicationScorer:
    def __init__(self, transcript: str):
        self.transcript = transcript.lower()

    def clarity_score(self):
        sentences = re.split(r"[.!?]", self.transcript)
        sentence_lengths = [len(s.split()) for s in sentences if s.strip()]
        if not sentence_lengths:
            return 0
        avg_len = np.mean(sentence_lengths)
        # Ideal avg sentence length: 8–18 words
        return max(0, 1 - abs(avg_len - 13) / 20)

    def conciseness_score(self):
        words = self.transcript.split()
        if len(words) < 50:
            return 1.0  # concise
        elif len(words) < 100:
            return 0.8
        elif len(words) < 200:
            return 0.6
        else:
            return 0.4  # too verbose

    def filler_word_penalty(self):
        count = sum(self.transcript.count(fw) for fw in FILLER_WORDS)
        return max(0, 1 - count * 0.05)

    def vocabulary_richness(self):
        words = [w for w in re.findall(r"\b\w+\b", self.transcript)]
        if not words:
            return 0
        unique_ratio = len(set(words)) / len(words)
        return min(1, unique_ratio * 3)  # normalized

    def final_score(self):
        clarity = self.clarity_score()
        conciseness = self.conciseness_score()
        filler = self.filler_word_penalty()
        vocab = self.vocabulary_richness()

        return {
            "clarity": round(clarity, 2),
            "conciseness": round(conciseness, 2),
            "filler": round(filler, 2),
            "vocabulary": round(vocab, 2),
            "overall": round((clarity + conciseness + filler + vocab) / 4, 2)
        }


if __name__ == "__main__":
    transcript = """
    Um, so I think like data analysis is, you know, basically about finding patterns.
    Actually, my background is in optimization, and I worked on big data processing
    and machine learning projects. I try to keep things concise and clear when I explain.
    """
    scorer = CommunicationScorer(transcript)
    print(scorer.final_score())

