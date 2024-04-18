""" The service module contains the business logic of the application. """

from django.core.files.uploadedfile import InMemoryUploadedFile
from flashcards.knowledge_base import response_formulation
from flashcards.rag_service import get_context, post_context
from flashcards.text_to_flashcards import Flashcard, generate_flashcards
from flashcards.text_scraper.text_extractor import TextExtractor
from flashcards.text_scraper.post_processing import Page


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


def process_answer(user_input: str) -> str:
    # This will answer a query only based on the list of closest correct answers from the data provided:

    # Generate the embedding for the user input
    curriculum = get_context(user_input)
    # Get a list of answers from the database

    # Use this list to generate a response
    answer_GPT = response_formulation(user_input, curriculum)

    return answer_GPT
