import openai
from flashcards.learning_resources import Flashcard, Page
from config import Config
from dataclasses import dataclass
from abc import ABC, ABCMeta, abstractmethod

api_key = Config().API_KEY
openai.api_key = api_key


class FlashcardGenerator(ABC):
    @abstractmethod
    def request_chat_completion(self, role: str, message: str) -> list[str]:
        """
        Returns a response from the LLM API

        Args:
            role (str, optional): The role of the message. Defaults to "system".
            message (str, optional): The message to be sent. Defaults to "".

        Returns:
            response (str): The response from the LLM API
        """
        pass


class OpenAIFlashcardGenerator(FlashcardGenerator):
    def request_chat_completion(role: str = "system", message: str = "") -> str:
        """
        Returns a response from the OpenAI API

        Args:
            role (str, optional): The role of the message. Defaults to "system".
            message (str, optional): The message to be sent. Defaults to "".

        Returns:
            response (str): The response from the OpenAI API
        """
        result = ""
        if not message:
            result = "Error: No message provided"
        else:
            response = openai.chat.completions.create(
                model=Config().GPT_MODEL, messages=[{"role": role, "content": message}]
            )
            result = response.choices[0].message.content
        return result


def generate_template(context: str) -> str:
    """
    Returns a template with the correct flashcard and prompt format which can be used to generate flashcards using the context

    Args:
        context (str): The sample text to be used

    Returns:
        str: The template with the correct flashcard and prompt format which can be used to generate flashcards using the context
    """

    example = f"Front: Which year was the person born? - Back: 1999 | Front: At what temperture does water boil? - Back: 100 degrees celsius | Front: MAC - Back: Message Authentication Code"
    template = f"Create a set of flashcards using the following format: {example} from the following text: {context}. Use only information from the text to generate the flashcards. Use only the given format. DO not use line breaks. Do not use any other format"

    return template


def parse_flashcard(flashcards_data: list[str], page: Page) -> list[Flashcard]:
    """
    Returns a list of the Flashcard dataclass

    Args:
        flashcards_data (list[str]): The flashcard to be parsed

    Returns:
        list[Flashcard]: A list of Flashcards with the front and back of the flashcard

    Example:
        [Flashcard(front="apple", back="banana"), Flashcard(front="orange", back="grape")]
    """
    flashcards = []

    for i in flashcards_data:
        if "Front: " not in i or "Back: " not in i or "-" not in i:
            continue

        i = i.replace("Front: ", "").replace("Back: ", "")
        i = i.split("-")
        flashcards.append(
            Flashcard(
                front=i[0].strip(),
                back=i[1].strip(),
                pdf_name=page.pdf_name,
                page_num=page.page_num,
            )
        )

    return flashcards


def generate_flashcards(page: Page) -> list[Flashcard]:
    """
    Returns a flashcard generated from the sample text

    Args:
        context (str): The sample text to be used

    Returns:
        list: The list of flashcards generated from the sample text
    """
    template = generate_template(page.text)
    response = OpenAIFlashcardGenerator.request_chat_completion(
        "system", message=template
    )
    response = response.split("|")
    return parse_flashcard(response, page)


def parse_for_anki(flashcards: list[Flashcard]) -> str:
    """
    Returns a string with the flashcards in the correct format for Anki

    Correct format: front:back
    Example: "apple:banana"

    Args:
        flashcards (list[Flashcard]): The flashcards to be parsed

    Returns:
        str: A string with the flashcards in the correct format for Anki
    """
    num_elements = len(flashcards)
    text = ""
    separator = "\n"

    for i in range(num_elements):
        front = flashcards[i].front
        back = flashcards[i].back

        text += front + ":" + back + separator

    return text
