from flashcards.textToFlashcards import request_chat_completion, generate_template, generate_flashcards, parse_flashcard


print(parse_flashcard(generate_flashcards()), flush=True)