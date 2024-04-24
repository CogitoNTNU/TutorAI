""" The service module contains the business logic of the application. """

from dataclasses import dataclass
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from flashcards.knowledge_base.response_formulation import response_formulation
from flashcards.knowledge_base.db_interface import MongoDB
from flashcards.rag_service import get_context, post_context
from flashcards.text_to_flashcards import Flashcard, generate_flashcards
from flashcards.text_scraper.text_extractor import TextExtractor
from flashcards.text_scraper.post_processing import Page
import comtypes.client

def process_flashcards(uploaded_file: InMemoryUploadedFile) -> list[Flashcard]:
    """
    Process the file and return the flashcards.
    """
    print("[INFO] Processing file", flush=True)

    # Extract text from the uploaded file
    extractor = TextExtractor()
    pages: list[Page] = extractor.extractData(uploaded_file)
    print("[INFO] Files read")
    flashcards: list[Flashcard] = []
    print("[INFO] Generating flashcards", flush=True)
    for page in pages:
        # TODO: Parallelize api calls
        flashcards_from_page = generate_flashcards(page)
        flashcards.extend(flashcards_from_page)

        # Save content
        post_context(page.text, page.page_num, page.pdf_name)

    return flashcards


        




def store_curriculum(uploaded_file: InMemoryUploadedFile) -> bool:
    """
    Process the file and store the pages as curriculum in a database.
    """
    print("[INFO] Processing file", flush=True)

    # Extract text from the uploaded file
    
    extractor = TextExtractor()
    pages: list[Page] = extractor.extractData(uploaded_file)

    for page in pages:
        # Save content
        context_posted: bool = post_context(page.text, page.page_num, page.pdf_name)
        # TODO: HANDLE FAILURE CASE OF POST CONTEXT
    return context_posted

def request_flashcards_by_page_range(pdf_name: str, page_num_start: int, page_num_end) -> list[Flashcard]:
    """
    Request flashcards for a specific page range and pdf from the database
    """
    # Get the flashcards from the database
    db = MongoDB()
    pages: list[Page] = db.get_page_range(pdf_name, page_num_start, page_num_end)
    flashcards: list[Flashcard] = []
    for page in pages:
        flashcards_from_page = generate_flashcards(page)
        flashcards.extend(flashcards_from_page)
    
    return flashcards

@dataclass
class RagAnswer:
    answer: str
    citations: list[Page]

    def to_dict(self) -> dict:
        return {
            "answer": self.answer,
            "citations": [citation.to_dict() for citation in self.citations],
        }


def process_answer(
    documents: list[str], user_question: str, chat_history: list[dict[str, str]]
) -> RagAnswer:
    # This will answer a query only based on the list of closest correct answers from the data provided:

    # Generate the embedding for the user input
    curriculum = []
    for document_name in documents:
        curriculum.extend(get_context(document_name, user_question))
    # Get a list of answers from the database

    # Use this list to generate a response
    answer_GPT = response_formulation(user_question, curriculum, chat_history)

    answer = RagAnswer(answer_GPT, curriculum)
    print(f"[INFO] Answer: {answer_GPT}", flush=True)

    return answer


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


def generate_quiz(document: str, start: int, end: int) -> Quiz:
    """
    Generates a quiz for the document
    """
    if start > end:
        raise ValueError(
            "The start index of the document can not be after then the end index!"
        )

    # Generate the quiz
    questions: list[QuestionAnswer] = []
    db = MongoDB()
    pages: list[Page] = db.get_page_range(document, start, end)
    for i in range(start, end):
        # TODO: use the text from the pages to generate questions
        questions.append(QuestionAnswer(f"Question {i}", f"Answer {i}"))

    return Quiz(document, start, end, questions)
