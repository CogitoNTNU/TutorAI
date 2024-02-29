import openai
from config import Config

api_key = Config().API_KEY

openai.api_key = api_key
sample_info = "Cristiano Ronaldo dos Santos Aveiro GOIH ComM (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all-time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player."


def request_chat_completion(previous_message: dict, role: str = "system", message: str = "", functions: list = []) -> list[str]: 
    """
    Returns a response from the OpenAI API

    Args:
        previous_message (dict): The previous message in the conversation
        role (str, optional): The role of the message. Defaults to "system".
        message (str, optional): The message to be sent. Defaults to "".
        functions (list, optional): The functions to be used. Defaults to [].
    
    Returns:
        response list[str]: The response from the OpenAI API
        if empty string, an error has occured
    """
    # TODO: Create this function
    return ""
    
def generate_template(sample_info: str = sample_info) -> str:
    """
    Returns a template with the correct flashcard and prompt format which can be used to generate flashcards using the sample text
    """
    # TODO: Create this function

    template = f"Create a set of flashcards from the following text: {sample_info}"

    return template

def generate_flashcards(sample_info: str = sample_info) -> str:
    """
    Returns a flashcard generated from the sample text

    Args:
        sample_info (str): The sample text to be used

    Returns:
        str: The flashcard generated from the sample text
    """
    # TODO: Create this function
    template = generate_template(sample_info)
    response = request_chat_completion({}, "system", template, [])
    return response
    
def parse_flashcard(flashcards_data: list[str]) -> list[dict[str, str]]:
    """
    Returns a list of dictionaries with the front and back of the flashcard

    Args:
        flashcards_data (list[str]): The flashcard to be parsed

    Returns:
        list[dict[str, str]]: A list of dictionaries with the front and back of the flashcard

    example:
        [{"front": "What is the capital of the USA?", "back": "Washington DC"}, {"front": "What is the capital of France?", "back": "Paris"}]

    """
    # TODO: Create this function
    
