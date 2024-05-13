from abc import ABC, abstractmethod
from dataclasses import dataclass

import openai

from config import Config


@dataclass
class Chat:
    role: str
    content: str


class TextGenerator(ABC):
    @abstractmethod
    def generate_response(
        self, role: str, message: str, history: list[Chat] = []
    ) -> str:
        """
        Returns a response from the LLM.

        Args:
            role (str): The role of the message
            message (str): The message to be sent
            history ("Chat", optional): The history of messages. Defaults to [].

        Returns:
            response (str): The response from the LLM
        """
        pass


class OpenAI(TextGenerator):
    """
    A class to generate text using the OpenAI API.
    This is a payment-based API so it requires an API key to use.
    """

    def generate_response(
        self, role: str, message: str, history: list[Chat] = []
    ) -> str:

        result = ""
        if not message:
            return "Error: No message provided"

        # Construct history
        messages = []
        for chat in history:
            messages.append(chat)
        messages.append({"role": role, "content": str(message)})
        # Send request to OpenAI
        response = openai.chat.completions.create(
            model=Config().GPT_MODEL,
            messages=messages,
        )
        result = response.choices[0].message.content
        return result
