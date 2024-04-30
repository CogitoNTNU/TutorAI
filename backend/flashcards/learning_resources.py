from dataclasses import dataclass


@dataclass
class Page:
    text: str
    page_num: int
    pdf_name: str

    def to_dict(self) -> dict:
        return {
            "text": self.text,
            "page_num": self.page_num,
            "pdf_name": self.pdf_name,
        }


@dataclass
class QuestionAnswer:
    question: str
    answer: str

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "answer": self.answer,
        }


@dataclass
class Quiz:
    # Metadata
    document: str
    start: int
    end: int

    # The list of questions
    questions: list[QuestionAnswer]

    def to_dict(self) -> dict:
        return {
            "document": self.document,
            "start": self.start,
            "end": self.end,
            "questions": [question.to_dict() for question in self.questions],
        }


@dataclass
class Compendium:
    # Metadata
    document_name: str
    start: int
    end: int
    key_concepts: list[str]
    summary: str

    def to_dict(self) -> dict:
        return {
            "document": self.document_name,
            "start": self.start,
            "end": self.end,
            "key_concepts": self.key_concepts,
            "summary": self.summary,
        }


@dataclass
class QuestionAnswer:
    question: str
    answer: str

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "answer": self.answer,
        }


@dataclass
class Quiz:
    # Metadata
    document: str
    start: int
    end: int

    # The list of questions
    questions: list[QuestionAnswer]

    def to_dict(self) -> dict:
        return {
            "document": self.document,
            "start": self.start,
            "end": self.end,
            "questions": [question.to_dict() for question in self.questions],
        }


@dataclass
class GradedQuiz:
    answers_was_correct: list[bool]
    feedback: list[str]

    def to_dict(self) -> dict:
        return {
            "answers_was_correct": self.answers_was_correct,
            "feedback": self.feedback,
        }


@dataclass
class RagAnswer:
    answer: str
    citations: list[Page]

    def to_dict(self) -> dict:
        return {
            "answer": self.answer,
            "citations": [citation.to_dict() for citation in self.citations],
        }


@dataclass
class Flashcard:
    front: str
    back: str
    pdf_name: str
    page_num: int

    def to_dict(self):
        return {
            "front": self.front,
            "back": self.back,
            "pdf_name": self.pdf_name,
            "page_num": self.page_num,
        }
