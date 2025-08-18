

import random

class QuestionGenerator:
    """
    A simple module to generate interview questions
    based on predefined categories (technical, behavioral, culture).
    """

    def __init__(self):
        self.questions = {
            "technical": [
                "Can you explain the difference between supervised and unsupervised learning?",
                "How would you optimize a machine learning model for imbalanced data?",
                "What is the role of feature engineering in improving model accuracy?",
                "Explain how you would preprocess a dataset with missing values.",
                "Describe a project where you applied data analysis to solve a real problem."
            ],
            "behavioral": [
                "Tell me about a time when you worked under pressure to meet a deadline.",
                "How do you approach solving a problem you’ve never seen before?",
                "Give an example of how you collaborated with a team to achieve success.",
                "What do you do when you disagree with a colleague’s idea?",
                "Describe a challenge you faced and how you overcame it."
            ],
            "culture": [
                "Why do you want to work with our company?",
                "What motivates you in a workplace?",
                "How do you handle feedback from peers or supervisors?",
                "What values are important to you when working in a team?",
                "How do you contribute to building a positive work culture?"
            ]
        }

    def generate(self, category: str, num_questions: int = 3):
        """
        Generate interview questions from a given category.
        
        :param category: 'technical', 'behavioral', or 'culture'
        :param num_questions: number of questions to return
        :return: list of selected questions
        """
        if category not in self.questions:
            raise ValueError(f"Unknown category: {category}. Choose from {list(self.questions.keys())}")
        
        return random.sample(self.questions[category], min(num_questions, len(self.questions[category])))


if __name__ == "__main__":
    qg = QuestionGenerator()
    
    print("Technical Questions:")
    for q in qg.generate("technical", 2):
        print(f"- {q}")
    
    print("\nBehavioral Questions:")
    for q in qg.generate("behavioral", 2):
        print(f"- {q}")
    
    print("\nCulture Fit Questions:")
    for q in qg.generate("culture", 2):
        print(f"- {q}")

