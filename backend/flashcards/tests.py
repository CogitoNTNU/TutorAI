from django.test import TestCase, Client
from flashcards.flashcard_service import process_answer
from flashcards.text_to_flashcards import (
    generate_flashcards,
    parse_for_anki,
    generate_template,
    OpenAIFlashcardGenerator,
    Flashcard,
)
from flashcards.text_scraper.post_processing import Page
import re
from rest_framework import status
from knowledge_base.response_formulation import response_formulation

base = "/api/"


# class TextToFlashcardTest(TestCase):
#     def setUp(self) -> None:
#         self.context = "Revenge of the Sith is set three years after the onset of the Clone Wars as established in Attack of the Clones. The Jedi are spread across the galaxy in a full-scale war against the Separatists. The Jedi Council dispatches Jedi Master Obi-Wan Kenobi on a mission to defeat General Grievous, the head of the Separatist army and Count Dooku's former apprentice, to put an end to the war. Meanwhile, after having visions of his wife Padmé Amidala dying in childbirth, Jedi Knight Anakin Skywalker is tasked by the Council to spy on Palpatine, the Supreme Chancellor of the Galactic Republic and, secretly, a Sith Lord. Palpatine manipulates Anakin into turning to the dark side of the Force and becoming his apprentice, Darth Vader, with wide-ranging consequences for the galaxy."
#
#     def test_openai_flashcard_generator(self):
#         template = generate_template(self.context)
#         response = OpenAIFlashcardGenerator.request_chat_completion(
#             "system", message=template
#         )
#         self.assertIsInstance(response, str)
#         self.assertNotEqual(response, "Error: No message provided")
#
#     def test_generate_flashcards(self):
#         page = Page(self.context, 1, "test.pdf")
#         flashcards = generate_flashcards(page)
#         self.assertIsInstance(flashcards, list)
#         self.assertIsInstance(flashcards[0], Flashcard)
#
#     def test_parse_for_anki(self):
#         page = Page(self.context, 1, "test.pdf")
#         flashcards = generate_flashcards(page)
#         anki_format = parse_for_anki(flashcards)
#         self.assertIsInstance(anki_format, str)
#         self.assertTrue(re.search("(.*:.*\n)*(.*:.*)", anki_format))
#
#     def process_answer_tapi  self.assertFalse(None, process_answer(user_input))


class RagAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = f"{base}search/"
        self.valid_pdf_name = "test.pdf"
        self.invalid_pdf_name = "invalid.pdf"
        self.valid_chat_history = [
            {"user": "What is the capital of India?", "response": "New Delhi"}
        ]
        self.valid_user_input = "This is a user input."
        self.valid_context = "The context."

    def test_invalid_request(self):
        invalid_payload = {}
        response = self.client.post(self.url, invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def invalid_pdf_name(self):
        pass

    def test_valid_request_without_chat_history(self):
        valid_response = {
            "pdf_name": self.valid_pdf_name,
            "user_question": "What is the capital of India?",
        }
        response = self.client.post(self.url, valid_response, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_request_with_chat_history(self):
        valid_response = {
            "pdf_name": self.valid_pdf_name,
            "user_question": "What is the capital of India?",
            "chat_history": self.valid_chat_history,
        }
        response = self.client.post(self.url, valid_response, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_class(self):
        valid_response = response_formulation(
            self.valid_user_input, self.valid_context, self.valid_chat_history
        )
        self.assertTrue(isinstance(valid_response, str))
