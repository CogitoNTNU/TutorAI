from abc import ABC, ABCMeta, abstractmethod
import openai
from config import Config

class EmbeddingsInterface(ABC):
    @abstractmethod
    def get_embedding(self, text, model):
        """
        Get the embedding of the text using the model

        Args:
            text (str): The text to be embedded
            model (str): The model to be used for embedding

        Returns:
            list[float]: The embedding of the text
        """
        pass

class Embeddings(EmbeddingsInterface):
    def __init__(self):
        api_key = Config().OPENAI_API_KEY
        self.client = openai.Client(api_key=api_key)

    def get_embedding(self, text, model="text-embedding-ada-002"):
        text = text.replace("\n", " ")
        response = self.client.embeddings.create(
            input=text,
            model=model
        )

        return response.data[0].embedding

if __name__ == "__main__":
    # Example use
    embeddings = Embeddings()

    print(embeddings.get_embedding("Hello world!!"))