from abc import ABC, abstractmethod
from flashcards.knowledge_base.embeddings import cosine_similarity
from config import Config
from pymongo import MongoClient


class DatabaseInterface(ABC):
    """
    Abstract class for Connecting to a Database
    """

    @classmethod
    def __instancecheck__(cls, instance: any) -> bool:
        return cls.__subclasscheck__(type(instance))

    @classmethod
    def __subclasscheck__(cls, subclass: any) -> bool:
        return (
            hasattr(subclass, "get_curriculum") and callable(subclass.get_curriculum)
        ) and (
            hasattr(subclass, "post_curriculum") and callable(subclass.post_curriculum)
        )

    @abstractmethod
    def get_curriculum(self, embedding: list[float]) -> list[str]:
        """
        Get the curriculum from the database

        Args:
            embedding (list[float]): The embedding of the question

        Returns:
            list[str]: The curriculum related to the question
        """
        pass

    @abstractmethod
    def post_curriculum(
        self, curriculum: str, page_num: int, paragraph_num: int, embedding: list[float]
    ) -> bool:
        """
        Post the curriculum to the database

        Args:
            curriculum (str): The curriculum to be posted
            embedding (list[float]): The embedding of the question

        Returns:
            bool: True if the curriculum was posted, False otherwise
        """
        pass

    @abstractmethod
    def get_source_reference(self, documents: list[str], curriculum: str) -> dict:
        '''
        Get source reference, which includes page number and pdf title

        Args:
            documents (list[str]): The list of strings that answers the question asked.
            curriculum (str): The entire curriculum that is posted.
        Returns:
            dict: Returns a dictionary with keys, "page number" and "pdf title"
        
        '''
        pass

class MongoDB(DatabaseInterface):
    def __init__(self):
        self.client = MongoClient(Config().MONGODB_URI)
        self.db = self.client["test-curriculum-database"]
        self.collection = self.db["test-curriculum-collection"]
        self.similarity_threshold = 0.83

    def get_curriculum(self, embedding: list[float]) -> list[str]:
        # Checking if embedding consists of decimals or "none"
        if not embedding:
            raise ValueError("Embedding cannot be None")

        # Define the MongoDB query that utilizes the search index "embeddings".
        query = {
            "$vectorSearch": {
                "index": "embeddings",
                "path": "embedding",
                "queryVector": embedding,
                "numCandidates": 30,  # MongoDB suggests using numCandidates=10*limit or numCandidates=20*limit
                "limit": 3,
            }
        }

        # Execute the query
        documents = self.collection.aggregate([query])

        if not documents:
            raise ValueError("No documents found")

        # Convert the documents to a list
        documents = list(documents)

        # Filter out the documents with low similarity
        for document in documents:
            if (
                cosine_similarity(embedding, document["embedding"])
                < self.similarity_threshold
            ):
                documents.remove(document)

        # Return the text content of the documents and page number
        documents = [{"text":document["text"],"pagenum":document["pageNum"]} for document in documents]
        documents[0]["pagenum"]
        return documents

    def post_curriculum(
        self, curriculum: str, page_num: int, paragraph_num: int, embedding: list[float]
    ) -> bool:
        if not curriculum:
            raise ValueError("Curriculum cannot be None")

        if not page_num:
            raise ValueError("Page number cannot be None")

        if not paragraph_num:
            raise ValueError("Paragraph number cannot be None")

        if not embedding:
            raise ValueError("Embedding cannot be None")

        try:
            # Insert the curriculum into the database with metadata
            self.collection.insert_one(
                {
                    "text": curriculum,
                    "pageNum": page_num,
                    "paragraphNum": paragraph_num,
                    "embedding": embedding,
                }
            )
            return True
        except:
            return False

    def get_source_reference(self, documents: list[str], curriculum: str) -> dict:
        for documents in curriculum:
            if documents == curriculum:
                page_number = documents[0]["pagenum"]
                pdf_title = None #TODO: Endre på denne
        return {"Page number": page_number, "pdf title": pdf_title}
            
