from app.core.llm import query_llm

class TutorAgent:
    def __init__(self, llm):
        self.llm = llm

    def explain_concept(self, topic: str) -> str:
        return self.llm(f"Teach me the concept of '{topic}' in a simple, clear way.")

    def generate_qcm(self, topic: str) -> str:
        return self.llm(f"Generate 3 MCQs with correct answers on '{topic}'.")

class ChallengerAgent:
    def __init__(self, llm):
        self.llm = llm

    def ask_question(self, topic: str) -> str:
        return self.llm(f"As a technical interviewer, ask a challenging question about '{topic}'.")

class MentorAgent:
    def __init__(self, llm):
        self.llm = llm

    def evaluate_answer(self, question: str, answer: str) -> str:
        return self.llm(
            f"You are my best version. Here's a technical question: '{question}'. "
            f"My answer: '{answer}'. Give me feedback on clarity, completeness, and improvement tips."
        )
