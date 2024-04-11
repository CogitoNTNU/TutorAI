""" Retrieval Augmented Generation Service """

from flashcards.knowledge_base.db_interface import DatabaseInterface
from flashcards.knowledge_base.embeddings import EmbeddingsInterface
from flashcards.knowledge_base.factory import create_database
from flashcards.knowledge_base.factory import create_embeddings_model



def get_context(
    query: str, db: DatabaseInterface, embeddings: EmbeddingsInterface
) -> list[str]:
    """
    Get the context of the query

    Args:
        query (str): The query to get the context of
        db (DatabaseInterface): The database to be used
        embeddings (EmbeddingsInterface): The embeddings to be used

    Returns:
        list[str]: The context of the query
    """
    embedding = embeddings.get_embedding(query)
    context = db.get_curriculum(embedding)
    return context


def post_context(
    context: str,
    page_num: int,
    paragraph_num: int,
) -> bool:
    """
    Post the context to the database

    Args:
        context (str): The context to be posted
        page_num (int): The page number of the context
        paragraph_num (int): The paragraph number of the context
        db (DatabaseInterface): The database to be used
        embeddings (EmbeddingsInterface): The embeddings to be used

    Returns:
        bool: True if the context was posted, False otherwise
    """
    db: DatabaseInterface = create_database()
    embeddings: EmbeddingsInterface = create_embeddings_model()

    embedding = embeddings.get_embedding(context)
    return db.post_curriculum(context, page_num, paragraph_num, embedding)
