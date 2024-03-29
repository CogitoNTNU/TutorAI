from django.test import TestCase
from flashcards.text_to_flashcards import generate_flashcards, parse_for_anki, generate_template, OpenAIFlashcardGenerator,  Flashcard
import re

class TextToFlashcardTest(TestCase):
    def setUp(self) -> None:
        self.context = "Revenge of the Sith is set three years after the onset of the Clone Wars as established in Attack of the Clones. The Jedi are spread across the galaxy in a full-scale war against the Separatists. The Jedi Council dispatches Jedi Master Obi-Wan Kenobi on a mission to defeat General Grievous, the head of the Separatist army and Count Dooku's former apprentice, to put an end to the war. Meanwhile, after having visions of his wife Padmé Amidala dying in childbirth, Jedi Knight Anakin Skywalker is tasked by the Council to spy on Palpatine, the Supreme Chancellor of the Galactic Republic and, secretly, a Sith Lord. Palpatine manipulates Anakin into turning to the dark side of the Force and becoming his apprentice, Darth Vader, with wide-ranging consequences for the galaxy."
    
    def test_openai_flashcard_generator(self):
        template = generate_template(self.context)
        response = OpenAIFlashcardGenerator.request_chat_completion("system", message=template)
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "Error: No message provided")
    
    def test_generate_flashcards(self):
        template = generate_template(self.context)
        flashcards = generate_flashcards(template)
        self.assertIsInstance(flashcards, list)
        self.assertIsInstance(flashcards[0], Flashcard)
    
    def test_parse_for_anki(self):
        flashcards = generate_flashcards(self.context)
        anki_format = parse_for_anki(flashcards)
        self.assertIsInstance(anki_format, str)
        self.assertTrue(re.search("(.*:.*\n)*(.*:.*)", anki_format) )

        
        

        