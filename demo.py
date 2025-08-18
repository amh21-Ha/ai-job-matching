# demo.py
"""
Common Demo for AI Recruitment & Fraud Detection Modules
Modules included:
1. Resume Matching
2. Interview AI (Q&A + Answer Evaluation)
3. Fraud Detection (Face Verification + Focus Monitoring)
4. Candidate Scoring (Technical, Communication, Culture)
"""

from resume_match.matcher import ResumeMatcher
from interview_ai.question_gen import QuestionGenerator
from interview_ai.answer_eval import AnswerEvaluator
from fraud_detection.face_verification import verify_face
from fraud_detection.focus_monitor import FocusMonitor
from scoring_engine.tech_scoring import score_technical
from scoring_engine.comm_scoring import CommunicationScorer
from scoring_engine.culture_scoring import CultureScorer


def demo_resume_matching():
    print("\n=== Resume Matching Demo ===")
    matcher = ResumeMatcher()
    job_desc = "Looking for a data analyst with Python, NLP, and ML experience."
    resume_text = "Experienced in Python, machine learning, NLP, and data analysis projects."
    score = matcher.match(job_desc, resume_text)
    print(f"Match Score: {score:.2f}")


def demo_interview_ai():
    print("\n=== Interview AI Demo ===")
    qg = QuestionGenerator()
    questions = qg.generate("technical", 2)
    print("Generated Technical Questions:")
    for q in questions:
        print(f"- {q}")

    evaluator = AnswerEvaluator()
    answer = "I have used Python and NLP for several data analysis projects."
    result = evaluator.score_answer("Explain your experience in NLP.", answer)
    print("Answer Evaluation:", result)


def demo_fraud_detection():
    print("\n=== Fraud Detection Demo ===")
    # Face verification example (requires images)
    try:
        verified, distance = verify_face("candidate_photo.jpg", "live_capture.jpg")
        print(f"Face Verified: {verified}, Distance: {distance:.2f}")
    except FileNotFoundError:
        print("Face images not found. Skipping face verification.")

    # Focus monitoring (live webcam)
    print("Starting Focus Monitor. Press 'q' to quit...")
    fm = FocusMonitor()
    fm.monitor_focus()


def demo_scoring_engine():
    print("\n=== Candidate Scoring Demo ===")
    # Technical
    test_results = {"coding": 80, "sql": 70, "ml": 90}
    tech_score = score_technical(test_results)
    print("Technical Score:", tech_score)

    # Communication
    transcript = "I have experience in Python, ML, and NLP. I try to be clear and concise."
    comm_scorer = CommunicationScorer(transcript)
    comm_scores = comm_scorer.final_score()
    print("Communication Scores:", comm_scores)

    # Culture
    answer = "I enjoy teamwork and coming up with creative solutions. I adapt well to changes."
    culture_scorer = CultureScorer()
    detailed_scores = culture_scorer.score_answer(answer)
    overall = culture_scorer.overall_score(answer)
    print("Culture Scores:", detailed_scores)
    print("Overall Culture Fit Score:", overall)


if __name__ == "__main__":
    demo_resume_matching()
    demo_interview_ai()
    demo_scoring_engine()
    # demo_fraud_detection()  # Uncomment if you want to test webcam and face verification

