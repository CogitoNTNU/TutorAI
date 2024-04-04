""" The service module contains the business logic of the application. """

from django.core.files.uploadedfile import InMemoryUploadedFile
from flashcards.rag_service import post_context
from flashcards.knowledge_base.factory import create_database
from flashcards.knowledge_base.factory import create_embeddings_model
from flashcards.text_to_flashcards import Flashcard, generate_flashcards
import flashcards.text_extractor as text_extractor

def process_flashcards(uploaded_file: InMemoryUploadedFile) -> list[Flashcard]:
    """
    Process the files and return the flashcards.
    """
    print("[INFO] Processing file", flush=True)

    # Extract text from the uploaded file
    # TODO: Use the scraper to extract the text from the uploaded file
    extractor = text_extractor.TextExtractor()
    extractor.extractParagraphs(uploaded_file)
    
    
    context: str = "hei"

    page_num = 1
    paragraph_num = 1
    db = create_database()
    embeddings = create_embeddings_model()

    # Post the text into knowledge base
    # TODO: Use the rag service to post the text into the knowledge base
    
    context_posted: bool = post_context(context, page_num, paragraph_num, db, embeddings)

    # Generate flashcards from the text
    # TODO: use the FlashcardGenerator to generate flashcards from the text

    flashcards = generate_flashcards(context)
    return flashcards
