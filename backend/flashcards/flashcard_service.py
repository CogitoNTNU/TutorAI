""" The service module contains the business logic of the application. """

from django.core.files.uploadedfile import InMemoryUploadedFile
from flashcards.rag_service import post_context
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
    for page in pages:
        # TODO: Parallelize api calls
        print("[INFO] Generating flashcards", flush=True)
        flashcards_from_page = generate_flashcards(page)
        flashcards.extend(flashcards_from_page)

        # Save content
        post_context(page.text, page.page_num, page.pdf_name)

    return flashcards


def store_curriculum(uploaded_file: InMemoryUploadedFile) -> bool:
    """
    Process the file and store the pages as curriculem in a database.
    """
    print("[INFO] Processing file", flush=True)

    # Extract text from the uploaded file
    extractor = TextExtractor()
    pages: list[Page] = extractor.extractData(uploaded_file)

    for index, page in enumerate(pages):
        # Save content
        context_posted: bool = post_context(page.text, page.page_num, page.pdf_name)

    return context_posted
