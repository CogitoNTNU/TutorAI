""" The service module contains the business logic of the application. """

from django.core.files.uploadedfile import InMemoryUploadedFile
from flashcards.rag_service import post_context
from flashcards.text_to_flashcards import Flashcard, generate_flashcards
from flashcards.text_scraper.text_extractor import TextExtractor
from flashcards.text_scraper.post_processing import PostProcessor, Data

from flashcards.knowledge_base.db_interface import DatabaseInterface
from flashcards.knowledge_base.embeddings import EmbeddingsInterface

def process_flashcards(uploaded_file: InMemoryUploadedFile) -> list[Flashcard]:
    """
    Process the files and return the flashcards.
    """
    print("[INFO] Processing file", flush=True)  

    # Extract text from the uploaded file
    # TODO: Use the scraper to extract the text from the uploaded file
    extractor = TextExtractor()
    paragraph_data: list[Data] = extractor.extractParagraphs(uploaded_file)
    
    for index, page in enumerate(paragraph_data):
        context: str = page.text
        page_num: int = page.page_num
        pdf_name: str = page.pdf_name
        if (page_num == None):
            raise Exception("Page number is null")
        if (context == None):
            continue
        if (pdf_name == None):
            raise Exception("PDF name is null")
        context_posted: bool = post_context(context, page_num, index)

    # Post the text into knowledge base
    # TODO: Use the rag service to post the text into the knowledge base
    

    # Generate flashcards from the text
    # TODO: use the FlashcardGenerator to generate flashcards from the text

    flashcards = generate_flashcards(context)
    return flashcards
