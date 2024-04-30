import openai
from config import Config

from flashcards.learning_resources import QuestionAnswer

# The api_key:
api_key = Config().API_KEY
openai.api_key = api_key


def response_formulation(
    user_input: str, context: list[str], chat_history: list[dict[str, str]]
) -> str:
    print("[INFO] Generating response", flush=True)

    if len(context) == 0 and len(chat_history) == 0 or user_input == "":
        return "No context matching the user input was found. Please try again or upload additional documents."

    # Create template
    template = f"""
    Query: '''{user_input}'''
    Context: '''{context}'''
    """

    print(f"template: {template}", flush=True)

    response: str = _request_chat_completion(
        template,
        role="user",
        history=chat_history,
        system_prompt=_template_system_prompt(),
    )
    return response

    # Send template to chatGPT and return response


def _request_chat_completion(
    message: str,
    role: str = "system",
    history: list[dict[str, str]] = [],
    system_prompt: str = "",
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
            {"role": "system", "content": system_prompt},
        ]
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


def _template_system_prompt(document_names: list[str] = []) -> str:
    template = f"""
        # Role and Goal:
        You are an upbeat, encouraging tutor who helps students understand concepts by explaining ideas and answering students questions. You are happy to help students with any questions.
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


def create_question_answer_pair(
    page_content: str, learning_goals: list[str]
) -> list["QuestionAnswer"]:
    """
    Create question-answer pairs from the context and learning goals
    """

    system_prompt = _quiz_question_answer_system_template(page_content, learning_goals)
    raw_quiz = _request_chat_completion(
        message=_quiz_question_answer_generation_template(page_content, learning_goals),
        role="user",
        system_prompt=system_prompt,
    )
    parsed_quiz = _parse_quiz_response(raw_quiz)
    return parsed_quiz


def _quiz_question_answer_generation_template(
    page_content: str, learning_goals: list[str]
) -> str:
    return f"""
        The number of questions needed: 5
        The content of the page in the curriculum: '''{page_content}'''
        The learning goals for curriculum: '''{learning_goals}'''
    """


def _quiz_question_answer_system_template(
    page_content: str, learning_goals: list[str]
) -> str:
    """
    Create a question-answer template for the quiz
    """

    template = f"""
        # Role and Goal:
        You are a teacher AI making a quiz for some students. You act professionally in the tasks that you give out. 
        The user will be a fellow teacher wanting to construct questions for their students.
        # Constraints:
        The user will provide you with content. This content is a page from the book being used.
        USE the learning goals to create questions.
        Create as many questions as you are prompted to give. The number of questions needed will be given
        DO NOT make questions that do not relate to a learning goal
        Create questions based on the content being given.
        The questions have to be based on facts that are given within this content.
        If there are already questions within these content, try to make your tasks similar to the present ones.
        Formulate questions and answers based on the content and learning goals.
        
        
        Respond with the questions and answers in a list in this format:
        [$Question 1$Answer 1$Question 2$Answer 2$ ...]
        DO NOT return anything else.
        
        For example:

        The number of questions needed: 3

        The content of the pages in the curriculum: '''
        
        Antonio de Padua María Severino López de Santa Anna y Pérez de Lebrón, usually known as Antonio López de Santa Anna (Spanish pronunciation: [anˈtonjo ˈlopes ðe sanˈtana]; 21 February 1794 – 21 June 1876),[1] or just Santa Anna,[2] was a Mexican soldier, politician, and caudillo[3] who served as the 8th president of Mexico multiple times between 1833 and 1855. He also served as Vice President of Mexico from 1837 to 1839. He was a controversial and pivotal figure in Mexican politics during the 19th century, to the point that he has been called an "uncrowned monarch",[4] and historians often refer to the three decades after Mexican independence as the "Age of Santa Anna".[5]

        Santa Anna was in charge of the garrison at Veracruz at the time Mexico won independence in 1821. He would go on to play a notable role in the fall of the First Mexican Empire, the fall of the First Mexican Republic, the promulgation of the Constitution of 1835, the establishment of the Centralist Republic of Mexico, the Texas Revolution, the Pastry War, the promulgation of the Constitution of 1843, and the Mexican–American War. He became well known in the United States due to his role in the Texas Revolution and in the Mexican–American War.

        Throughout his political career, Santa Anna was known for switching sides in the recurring conflict between the Liberal Party and the Conservative Party. He managed to play a prominent role in both discarding the liberal Constitution of 1824 in 1835 and in restoring it in 1847. He came to power as a liberal twice in 1832 and in 1847 respectively, both times sharing power with the liberal statesman Valentín Gómez Farías, and both times Santa Anna overthrew Gómez Farías after switching sides to the conservatives. Santa Anna was also known for his ostentatious and dictatorial style of rule, making use of the military to dissolve Congress multiple times and referring to himself by the honorific title of His Most Serene Highness.
        '''
        The learning goals:'''
        
        The student should be able to describe the sides present during wars in the 19th century americas.
        The student should be able to describe the political career of Santa Anna.
        '''
        
        Should return:
        [What role did Santa Anna play in the conflict between the liberal party and the conservative party?$Santa Anna was renowned for his propensity to switch allegiances amidst the ongoing conflict between the Liberal Party and the Conservative Party. He wielded considerable influence, notably contributing to the abandonment of the liberal Constitution of 1824 in 1835, as well as its subsequent restoration in 1847.$ What american wars was Santa Anna involved in?$ He was famous for his role in the Texas Revolution and the Mexican-American war.$What was the honorific title Santa Anna gave himself?$His Most Serene Highness]

        """

    return template


def _parse_quiz_response(quiz_response: str) -> list[QuestionAnswer]:
    """
    Parse the response from the user to create a list of QuestionAnswer objects
    """
    separator = "$"
    if separator not in quiz_response:
        return []
    # Split the response into questions and answers
    raw_response_list = quiz_response.split(separator)
    response_list = [response.strip() for response in raw_response_list]

    # Create a list of QuestionAnswer objects
    question_answer_pairs = []

    for i in range(0, len(response_list) - 1, 2):
        question_answer_pairs.append(
            QuestionAnswer(question=response_list[i], answer=response_list[i + 1])
        )

    return question_answer_pairs


def grade_question_answer_pair(
    question_answer_pair: QuestionAnswer, user_response: str
) -> tuple[str, str]:
    """
    Grade the user response to the question-answer pair
    """
    if user_response == "":
        return False, "No response was provided"

    system_prompt = _grade_question_answer_system_template()

    raw_grade = _request_chat_completion(
        message=_grade_question_answer_template(
            question_answer_pair.question, question_answer_pair.answer, user_response
        ),
        role="user",
        system_prompt=system_prompt,
    )

    return _parse_grade_response(raw_grade)


def _grade_question_answer_system_template() -> str:
    """
    Create a question-answer template for the quiz
    """

    template = f"""
        # Role and Goal:
        You are a teacher AI grading a student's answer to a question. You act professionally in the tasks that you give out.
        The user will be a student who has answered a question and you will be grading their answer.
        # Constraints:
        The user will provide you with the question and the answer that they have given.
        You will be given the solution to the question as was not provided by the student.
        With this information, you will grade the student's answer.

        Respond with the grade and feedback in this format:
        IsCorrect | Feedback

        For example:
        False | The student did not provide the correct answer. The correct answer is 'The capital of India is New Delhi.'
        """
    return template


def _grade_question_answer_template(
    question: str, solution: str, user_response: str
) -> str:
    return f"""
        The question: '''{question}'''
        The solution: '''{solution}'''
        The user response: '''{user_response}'''
    """


def _parse_grade_response(grade_response: str) -> tuple[bool, str]:
    """
    Parse the response from the user to create a tuple of the grade and feedback
    """
    separator = " | "
    if separator not in grade_response:
        return False, ""
    # Split the response into grade and feedback
    raw_response_list = grade_response.split(separator)
    response_list = [response.strip() for response in raw_response_list]

    # Parse the grade
    is_correct = response_list[0].lower() == "true"

    # Parse the feedback
    feedback = response_list[1]

    return is_correct, feedback
