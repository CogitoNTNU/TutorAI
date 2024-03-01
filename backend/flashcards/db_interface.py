from abc import ABC, ABCMeta, abstractmethod
from pymongo import MongoClient

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
        '''    
        pass

class Database(DatabaseInterface):
    def __init__(self):
        self.client = MongoClient('mongodb+srv://olav:olav@development.i1eraq8.mongodb.net/')
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

        # Make simple functionality to return the single document that is stored in this collection
        return self.collection.find_one({})

    def post_curriculum(self, curriculum: str, embedding: list[float]) -> None:
        '''
        Post the curriculum to the database

        Args:
            curriculum (str): The curriculum to be posted
            embedding (list[float]): The embedding of the question
        '''

        # Make simple functionality to insert a document into the collection, which has the _id field and a text field
        self.collection.insert_one({'text': curriculum})
    
# Test the get_curriculum method
if __name__ == '__main__':
    db = Database()
    print(db.get_curriculum([1.0, 2.0, 3.0]))

    # Test the post_curriculum method
    curriculum = input('Enter a curriculum: ')
    db.post_curriculum(curriculum, [1.0, 2.0, 3.0])
