""" The service module contains the business logic of the application. """

from django.core.files.uploadedfile import InMemoryUploadedFile


def process_flashcards(uploaded_file: InMemoryUploadedFile) -> list["Flashcard"]:
    """
    Process the files and return the flashcards.
    """
    print("[INFO] Processing file", flush=True)

    # Extract text from the uploaded file
    # TODO: Use the scraper to extract the text from the uploaded file
    
    text: str = ""

    # Post the text into knowledge base
    # TODO: Use the rag service to post the text into the knowledge base
    

    # Generate flashcards from the text
    # TODO: use the FlashcardGenerator to generate flashcards from the text

