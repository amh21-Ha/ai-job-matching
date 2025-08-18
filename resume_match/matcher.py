from sentence_transformers import SentenceTransformer, util

class ResumeMatcher:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def match(self, job_desc: str, resume_text: str) -> float:
        embeddings = self.model.encode([job_desc, resume_text], convert_to_tensor=True)
        similarity = util.cos_sim(embeddings[0], embeddings[1])
        return float(similarity)

