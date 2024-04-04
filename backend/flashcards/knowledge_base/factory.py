from flashcards.knowledge_base.db_interface import DatabaseInterface, MongoDB
from flashcards.knowledge_base.embeddings import EmbeddingsInterface, OpenAIEmbedding


def create_database(database_system: str = "mongodb") -> DatabaseInterface:
    match database_system.lower():
        case "mongodb":
            return MongoDB()
        case _:
            raise ValueError(f"Database system {database_system} not supported")


def create_embeddings_model(embeddings_model: str = "openai") -> EmbeddingsInterface:
    match embeddings_model.lower():
        case "openai":
            return OpenAIEmbedding()
        case _:
            raise ValueError(f"Embeddings model {embeddings_model} not supported")
