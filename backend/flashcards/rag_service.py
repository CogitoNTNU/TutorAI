""" Retrieval Augmented Generation Service """

from flashcards.learning_resources import Page
from flashcards.knowledge_base.db_interface import Database
from flashcards.knowledge_base.embeddings import EmbeddingsModel
from flashcards.knowledge_base.factory import create_database
from flashcards.knowledge_base.factory import create_embeddings_model


db: Database = create_database()
embeddings: EmbeddingsModel = create_embeddings_model()


def get_context(pdf_name: str, query: str) -> list[Page]:
    """
    Get the context of the query

    Args:
        query (str): The query to get the context of

    Returns:
        list[str]: The context of the query
    """
    embedding = embeddings.get_embedding(query)
    context = db.get_curriculum(pdf_name, embedding)
    return context


def get_page_range(
    pdf_name: str,
    page_num_start: int,
    page_num_end: int,
) -> list[Page]:
    """
    Get the context of the query

    Args:
        pdf_name (str): The name of the pdf
        page_num_start (int): The start page number
        page_num_end (int): The end page number
    Returns:
        list[str]: The context of the query
    """
    return db.get_page_range(pdf_name, page_num_start, page_num_end)


def post_context(
    context: str,
    page_num: int,
    pdf_name: str,
) -> bool:
    """
    Post the context to the database

    Args:
        context (str): The context to be posted
        page_num (int): The page number of the context
        paragraph_num (int): The paragraph number of the context

    Returns:
        bool: True if the context was posted, False otherwise
    """

    embedding = embeddings.get_embedding(context)
    return db.post_curriculum(context, page_num, pdf_name, embedding)
