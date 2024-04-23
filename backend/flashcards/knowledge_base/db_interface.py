from abc import ABC, abstractmethod
from .embeddings import OpenAIEmbedding, cosine_similarity
from config import Config
from pymongo import MongoClient
from flashcards.text_scraper.post_processing import Page


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
    def get_curriculum(self, pdf_name: str, embedding: list[float]) -> list[Page]:
        """
        Get the curriculum from the database

        Args:
            embedding (list[float]): The embedding of the question
            pdf_name (str): The name of the pdf to use

        Returns:
            list[str]: The curriculum related to the question
        """
        pass

    @abstractmethod
    def get_page_range(
        self, pdf_name: str, page_num_start: int, page_num_end: int
    ) -> list[Page]:
        """
        Retrieves a range of pages from the knowledge base.

        Args:
            page_num_start (int): The starting page number (inclusive).
            page_num_end (int): The ending page number (inclusive).

        Returns:
            list[Curriculum]: A list of Curriculum objects representing pieces of content, like sentences, the specified page range.
        """
        pass

    @abstractmethod
    def post_curriculum(
        self, curriculum: str, page_num: int, pdf_name: str, embedding: list[float]
    ) -> bool:
        """
        Post the curriculum to the database

        Args:
            curriculum (str): The curriculum to be posted
            embedding (list[float]): The embedding of the page

        Returns:
            bool: True if the curriculum was posted, False otherwise
        """
        pass

    @abstractmethod
    def delete_all_curriculum(self) -> bool:
        """
        Delete all curriculum from the database

        Returns:
            bool: True if the curriculum was deleted, False otherwise
        """
        pass

class MongoDB(DatabaseInterface):
    def __init__(self, uri=Config().MONGODB_URI):
        self.client = MongoClient(uri)
        self.db = self.client["test-curriculum-database"]
        self.collection = self.db["test-curriculum-collection"]
        self.similarity_threshold = 0.7
        self.embeddings = OpenAIEmbedding()

    def get_curriculum(self, pdf_name: str, embedding: list[float]) -> list[Page]:
        # Checking if embedding consists of decimals or "none"
        if not embedding:
            raise ValueError("Embedding cannot be None")

        # Define the MongoDB query that utilizes the search index "embeddings".
        query = {
            "$vectorSearch": {
                "index": "embeddings",
                "path": "embedding",
                "queryVector": embedding,
                # MongoDB suggests using numCandidates=10*limit or numCandidates=20*limit
                "numCandidates": 30,
                "limit": 3,
            }
        }

        # Execute the query
        documents = self.collection.aggregate([query])

        if not documents:
            raise ValueError("No documents found")

        # Convert the documents to a list
        documents = list(documents)

        results = []

        # Filter out the documents with low similarity
        for document in documents:
            threshold = self.similarity_threshold
            if (
                cosine_similarity(embedding, document["embedding"])
                > self.similarity_threshold
            ):
                results.append(
                    Page(
                        text=document["text"],
                        page_num=document["pageNum"],
                        pdf_name=document["pdfName"],
                    )
                )

        return results

    def get_page_range(
        self, pdf_name: str, page_num_start: int, page_num_end: int
    ) -> list[Page]:
        # Get the curriculum from the database
        cursor = self.collection.find(
            {
                "pdfName": pdf_name,
                "pageNum": {"$gte": page_num_start, "$lte": page_num_end},
            }
        )

        if not cursor:
            raise ValueError("No documents found")

        results = []

        for document in cursor:
            results.append(
                Page(
                    text=document["text"],
                    page_num=document["pageNum"],
                    pdf_name=document["pdfName"],
                )
            )

        return results

    def post_curriculum(
        self, curriculum: str, page_num: int, pdf_name: str, embedding: list[float]
    ) -> bool:
        if not curriculum:
            raise ValueError("Curriculum cannot be None")

        if page_num == None:
            raise ValueError("Page number cannot be None")

        if pdf_name == None:
            raise ValueError("Paragraph number cannot be None")

        if not embedding:
            raise ValueError("Embedding cannot be None")

        if not pdf_name:
            raise ValueError("PDF name cannot be None")

        try:
            # Insert the curriculum into the database with metadata
            self.collection.insert_one(
                {
                    "text": curriculum,
                    "pageNum": page_num,
                    "pdfName": pdf_name,
                    "embedding": embedding,
                    "pdfName": pdf_name,
                }
            )
            return True
        except:
            return False

    def delete_all_curriculum(self) -> bool:
        """
        Delete all curriculum from the database

        Returns:
            bool: True if all curriculum were deleted, False otherwise
        """
        try:
            # Deleting all documents from MongoDB collection
            self.collection.delete_many({})
            return True
        except Exception as e:
            print("Error deleting curriculum:", e)
            return False
    
    def delete_pdf_pages(self, pdf_name: str) -> bool:
        """
        Delete all curriculum entries with a specific PDF name from the database

        Args:
            pdf_name (str): The PDF name to match for deletion

        Returns:
            bool: True if all matching curriculum entries were deleted, False otherwise
        """
        try:
            # Deleting documents from MongoDB collection based on a condition
            self.collection.delete_many({"pdfName": pdf_name})
            return True
        except Exception as e:
            print("Error deleting curriculum:", e)
            return False