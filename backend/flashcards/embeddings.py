from abc import ABC, ABCMeta, abstractmethod
import openai
from config import Config
import numpy as np

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
        api_key = Config().API_KEY
        self.client = openai.Client(api_key=api_key)

    def get_embedding(self, text, model="text-embedding-ada-002"):
        text = text.replace("\n", " ")
        response = self.client.embeddings.create(
            input=text,
            model=model
        )

        return response.data[0].embedding
    
    def cosine_similarity(self, embedding1, embedding2):
        sum_times = 0
        embedding1_sq = 0
        embedding2_sq = 0
        for i in range(len(embedding1)):
            sum_times += embedding1[i]*embedding2[i]
            embedding1_sq += embedding1[i]**2
            embedding2_sq += embedding2[i]**2
        root_times_emb1_emb2 = np.sqrt(embedding1_sq*embedding2_sq)
        return sum_times/root_times_emb1_emb2

if __name__ == "__main__":
    # Example use
    embeddings = Embeddings()

    embedding1 = embeddings.get_embedding("The Rock")
    embedding2 = embeddings.get_embedding("Dwayne Johnson")
    print(embeddings.cosine_similarity(embedding1, embedding2))
