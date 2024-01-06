import openai
# from config import Config

# api_key = Config().API_KEY

scuffed_key = "key"
openai.api_key = scuffed_key

def request_chat_completion(previous_message: dict, role: str = "system", message: str = "", functions: list = []): 

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

sample_info = "Cristiano Ronaldo dos Santos Aveiro GOIH ComM (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all-time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player."

example_flashcard = "(What is the capital of France? - Paris) | (Why is is coffe good? - Because it is tasty.) | (Who was the first man on the moon - Lance Armstrong)"
template = f"Generate a set flashcard with this format {example_flashcard} about the most important part of this sample text: {sample_info}. Use only information from the sample text. Use only the format given.  "
result = request_chat_completion(None, 'system', template)
result = result.split('|')
print(result)