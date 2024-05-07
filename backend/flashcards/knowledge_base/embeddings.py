from abc import ABC, abstractmethod
import openai
from config import Config
import numpy as np


class EmbeddingsModel(ABC):
    @abstractmethod
    def get_embedding(self, text: str) -> list[float]:
        """
        Get the embedding of the text using the model

        Args:
            text (str): The text to be embedded
            model (str): The model to be used for embedding

        Returns:
            list[float]: The embedding of the text
        """
        pass


class OpenAIEmbedding(EmbeddingsModel):
    def __init__(self, model_name: str = "text-embedding-ada-002"):
        api_key = Config().API_KEY
        self.client = openai.Client(api_key=api_key)
        self.model_name = model_name

    def get_embedding(self, text: str) -> list[float]:
        text = text.replace("\n", " ")
        response = self.client.embeddings.create(input=text, model=self.model_name)
        return response.data[0].embedding


def cosine_similarity(embedding1: list[float], embedding2: list[float]) -> float:
    """
    Calculate the cosine similarity between two embeddings

    Args:
        embedding1 (list[float]): The first embedding
        embedding2 (list[float]): The second embedding

    Returns:
        float: The cosine similarity between the two embeddings
    """
    sum_times = 0
    embedding1_sq = 0
    embedding2_sq = 0
    for i in range(len(embedding1)):
        sum_times += embedding1[i] * embedding2[i]
        embedding1_sq += embedding1[i] ** 2
        embedding2_sq += embedding2[i] ** 2
    root_times_emb1_emb2 = np.sqrt(embedding1_sq * embedding2_sq)
    return sum_times / root_times_emb1_emb2
