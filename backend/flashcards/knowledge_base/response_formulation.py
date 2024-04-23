from json import dumps
import openai
from config import Config

# Design a function that takes in context, query, chatGPT model & returns an answer that will be outputted to TuturAI in the form of a string

# The api_key:
api_key = Config().API_KEY
openai.api_key = api_key


def response_formulation(
    user_input: str, context: list[str], chat_history: list[dict]
) -> str:
    print("[INFO] Generating response", flush=True)

    context_str = dumps(context, indent=2)
    chat_history_str = dumps(chat_history, indent=2)

    # Create template
    template = f"""
    You are TutorAI, and this is what the user wrote to ask you. 
    {user_input}: 
    {context}: This is the context you were given, so formulate an answer that answers the question.
    {chat_history}: This contains a list of chat history.
    """

    print(f"template: {template}", flush=True)

    response: str = _request_chat_completion(template, role="user")
    return response

    # Send template to chatGPT and return response


def _request_chat_completion(message: str, role: str = "system") -> str:
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
