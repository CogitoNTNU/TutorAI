from abc import ABC, ABCMeta, abstractmethod
from config import Config
from pymongo import MongoClient
from embeddings import Embeddings

class DatabaseInterface(ABC):
    '''
    Abstract class for Connecting to a Database
    '''
    @classmethod
    def __instancecheck__(cls, instance: any) -> bool:
        return cls.__subclasscheck__(type(instance))
    
    @classmethod
    def __subclasscheck__(cls, subclass: any) -> bool:
        return (
            hasattr(subclass, 'get_curriculum') and
            callable(subclass.get_curriculum)
        )
    
    @abstractmethod
    def get_curriculum(self, embedding: list[float]) -> str:
        '''
        Get the curriculum from the database

        Args:
            embedding (list[float]): The embedding of the question

        Returns:
            str: The curriculum related to the question
        '''
        pass

    @abstractmethod
    def post_curriculum(self, curriculum: str, embedding: list[float]) -> None:
        '''
        Post the curriculum to the database

        Args:
            curriculum (str): The curriculum to be posted
            embedding (list[float]): The embedding of the question

        Returns:
            bool: True if the curriculum was posted, False otherwise
        '''    
        pass

class Database(DatabaseInterface):
    def __init__(self):
        self.client = MongoClient(Config().MONGODB_CONNECTION_STRING)
        self.db = self.client['test-curriculum-database']
        self.collection = self.db['test-curriculum-collection']

    def get_curriculum(self, embedding: list[float]) -> str:
        '''
        Get the curriculum from the database

        Args:
            embedding (list[float]): The embedding of the question

        Returns:
            str: The curriculum related to the question
        '''
        # Define the query
        query = {
            "$vectorSearch": {
                "index": "conversationsIndex",
                "path": "conversationEmbedding",
                "queryVector": embedding,
                "numCandidates": 2,
                "limit": 1
            }
        }

        # Execute the query
        documents = list(self.collection.aggregate([query]))

        print(documents)
        # Make simple functionality to return the single document that is stored in this collection
        return self.collection.find_one({})

    def post_curriculum(self, curriculum: str, page_num: int, paragraph_num: int, embedding: list[float]) -> bool:
        '''
        Post the curriculum to the database

        Args:
            curriculum (str): The curriculum to be posted
            embedding (list[float]): The embedding of the question
        '''

        if curriculum == None:
            raise ValueError('Curriculum cannot be None')

        if page_num == None:
            raise ValueError('Page number cannot be None')
        
        if embedding == None:
            raise ValueError('Embedding cannot be None')

        try:
            self.collection.insert_one({'text': curriculum, 'pageNum': page_num, 'paragraphNum': paragraph_num, 'embedding': embedding})
            return True
        except:
            return False
    
# Test the get_curriculum method
if __name__ == '__main__':

    db = Database()
    
    # Test the get_curriculum method
    # curriculum = db.get_curriculum(embedding=[0.5, 0.5])
    # print(curriculum)

    # Test the post_curriculum method
    curriculum = input('Enter a curriculum: ')
    embeddings = Embeddings()
    embedding = embeddings.get_embedding(text=curriculum)
    print(db.post_curriculum(curriculum=curriculum, page_num=1, paragraph_num=4, embedding=embedding))
