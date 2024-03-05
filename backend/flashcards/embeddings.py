from abc import ABC, ABCMeta, abstractmethod
from openai import OpenAI

class EmbeddingsInterface(ABC):
    @abstractmethod
    def get_embedding(self, text, model):
        pass

class Embeddings(EmbeddingsInterface):
    def __init__(self):
        self.client = OpenAI()

    def get_embedding(self, text, model="text-embedding-ada-002"):
        text = text.replace("\n", " ")
        response = self.client.embeddings.create(
            input=text,
            model=model
        )

        return response

if __name__ == "__main__":
    # Example use
    embeddings = Embeddings()

    print(embeddings.get_embedding("Hello world!!"))