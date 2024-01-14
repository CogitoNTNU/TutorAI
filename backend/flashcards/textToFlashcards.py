import openai
from config import Config

api_key = Config().API_KEY

openai.api_key = api_key
sample_info = "Cristiano Ronaldo dos Santos Aveiro GOIH ComM (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all-time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player."


def request_chat_completion(previous_message: dict, role: str = "system", message: str = "", functions: list = []) -> str: 
    """
    Returns a response from the OpenAI API

    Args:
        previous_message (dict): The previous message in the conversation
        role (str, optional): The role of the message. Defaults to "system".
        message (str, optional): The message to be sent. Defaults to "".
        functions (list, optional): The functions to be used. Defaults to [].
    
    Returns:
        response (str): The response from the OpenAI API
    """
    try:
        if(not (role == "system" or "user" or "assistant")):
            print("Invalid role")
            return ""
        
        if(previous_message):
            response = openai.chat.completions.create(
                model = "gpt-4",
                messages = [
                    previous_message,
                    {"role": role, "content": message}
                ], 
                functions = functions
            )
        else: 
            response = openai.chat.completions.create(
                model = "gpt-4",
                messages=[
                    {"role": role, "content": message}, 
                ]
            )
        return response.choices[0].message.content
    
    except Exception as error: 
        print(f"An error has occured while requesting chat completion.")
        print(f"The error: {str(error)}")
        return ""
    
def generate_template(sample_info: str) -> str:
    """
    Returns a template with the correct flashcard and prompt format which can be used to generate flashcards using the sample text
    """
    example_flashcard = "What is the capital of France? - Paris | Why is is coffe good? - Because it is tasty. | Who was the first man on the moon - Lance Armstrong"
    template = f"Generate a set flashcard with this format {example_flashcard} about the most important part of this sample text: {sample_info}. Use only information from the sample text. Use only the format given.  "

    return template

def generate_flashcards(sample_info: str = sample_info) -> str:
    """
    Returns a flashcard generated from the sample text

    Args:
        sample_info (str): The sample text to be used

    Returns:
        str: The flashcard generated from the sample text
    """
    template = generate_template(sample_info)

    result = request_chat_completion(None, 'system', template)
    result = result.split('|')

    return result
def parse_flashcard(flashcard: str) -> list[dict[str, str]]:
    """
    Returns a list of dictionaries with the front and back of the flashcard

    Args:
        flashcard (str): The flashcard to be parsed

    Returns:
        list[dict[str, str]]: A list of dictionaries with the front and back of the flashcard

    example:
        [{"front": "What is the capital of the USA?", "back": "Washington DC"}, {"front": "What is the capital of France?", "back": "Paris"}]

    """
    parse_flashcard = []
    separator = '-'
    
    for card in flashcard:
        card = {
            "front": card.split(separator)[0].strip(),
            "back": card.split(separator)[1].strip()
        }
        parse_flashcard.append(card)

    return parse_flashcard
