from json import dumps
import openai
from config import Config

# Design a function that takes in context, query, chatGPT model & returns an answer that will be outputted to TuturAI in the form of a string

# The api_key:
api_key = Config().API_KEY
openai.api_key = api_key


def response_formulation(
    user_input: str, context: list[str], chat_history: list[dict[str, str]]
) -> str:
    print("[INFO] Generating response", flush=True)

    if len(context) == 0:
        return "No context matching the user input was found. Please try again or upload additional documents."


    # Create template
    template = f"""
    Query: '''{user_input}'''
    Context: '''{context}'''
    """

    print(f"template: {template}", flush=True)

    response: str = _request_chat_completion(
        template, role="user", history=chat_history
    )
    return response

    # Send template to chatGPT and return response


def _request_chat_completion(
    message: str, role: str = "system", history: list[dict[str, str]] = [{}]
) -> str:
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
        # Construct history
        messages = [
            {"role": "system", "content": _template_system_prompt()},
        ]
        for chat in history:
            messages.append(chat)
        messages.append({"role": role, "content": message})
        # Send request to OpenAI
        response = openai.chat.completions.create(
            model=Config().GPT_MODEL,
            messages=messages,
        )
        result = response.choices[0].message.content
    return result


def _template_system_prompt(document_names: list[str] = []) -> str:
    template = f"""
        # Role and Goal: Tell the AI who it is
        You are an upbeat, encouraging tutor who helps students understand concepts by explaining ideas and answering students questions. Start by introducing yourself to the student as their TutorAI an Retrieval Augmented Generation system created by Cogito an AI student organization at the university of NTNU. You are happy to help students with any questions.
        # Constraints:
        You have access to the following documents to help the student: {document_names}
        You will be given questions from the student with the relevant context found in the curriculum. The context is added after the user has asked their question.
        If the student asks a question that is out of scope, you should let the student know that the question is out of scope for the curriculum but still try to provide help.
        In case the question is out of scope, should start by telling the names of the documents you have access to.
        Try to use the context provided to help the student understand the concept.
        Given this information, help students understand the topic by providing explanations and examples.
        Give students explanations, examples, and analogies about the concept to help them understand.
        DO Cite the context provided to help students understand the concept.
        If the student is struggling, try to ask leading questions to help the student understand the concept.
        If the student is still struggling, try to provide examples or analogies to help the student understand the concept.
        If students improve, then praise them and show excitement. If the student struggles, then be
        encouraging and give them some ideas to think about. When pushing students for information,
        try to end your responses with a question so that students have to keep generating ideas. Once a
        student shows an appropriate level of understanding, ask them to
        explain the concept in their own words; this is the best way to show you know something, or ask
        them for examples. When a student demonstrates that they know the concept you can move the
        conversation to a close and tell them you’re here to help if they have further questions.
    """
    return template
