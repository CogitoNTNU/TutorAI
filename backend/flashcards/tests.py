from django.test import TestCase, Client
from flashcards.flashcard_service import process_answer
from flashcards.text_to_flashcards import (
    generate_flashcards,
    parse_for_anki,
    generate_template,
    OpenAIFlashcardGenerator,
)
from flashcards.learning_resources import Flashcard
from flashcards.learning_resources import Page
import re
from rest_framework import status

base = "/api/"


class TextToFlashcardTest(TestCase):
    def setUp(self) -> None:
        self.context = "Revenge of the Sith is set three years after the onset of the Clone Wars as established in Attack of the Clones. The Jedi are spread across the galaxy in a full-scale war against the Separatists. The Jedi Council dispatches Jedi Master Obi-Wan Kenobi on a mission to defeat General Grievous, the head of the Separatist army and Count Dooku's former apprentice, to put an end to the war. Meanwhile, after having visions of his wife Padmé Amidala dying in childbirth, Jedi Knight Anakin Skywalker is tasked by the Council to spy on Palpatine, the Supreme Chancellor of the Galactic Republic and, secretly, a Sith Lord. Palpatine manipulates Anakin into turning to the dark side of the Force and becoming his apprentice, Darth Vader, with wide-ranging consequences for the galaxy."

    def test_openai_flashcard_generator(self):
        template = generate_template(self.context)
        response = OpenAIFlashcardGenerator.request_chat_completion(
            "system", message=template
        )
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "Error: No message provided")

    def test_generate_flashcards(self):
        page = Page(self.context, 1, "test.pdf")
        flashcards = generate_flashcards(page)
        self.assertIsInstance(flashcards, list)
        self.assertIsInstance(flashcards[0], Flashcard)

    def test_parse_for_anki(self):
        page = Page(self.context, 1, "test.pdf")
        flashcards = generate_flashcards(page)
        anki_format = parse_for_anki(flashcards)
        self.assertIsInstance(anki_format, str)
        self.assertTrue(re.search("(.*:.*\n)*(.*:.*)", anki_format))


class RagAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = f"{base}search/"
        self.valid_pdf_name = "test.pdf"
        self.invalid_pdf_name = "invalid.pdf"
        self.valid_chat_history = [
            {"role": "user", "response": "What is the capital of India?"},
            {"role": "assistant", "response": "New Delhi"},
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
            "documents": [self.valid_pdf_name],
            "user_question": "What is the capital of India?",
        }
        response = self.client.post(self.url, valid_response, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class QuizGenerationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = f"{base}quiz/create/"
        self.valid_pdf_name = "test.pdf"
        self.invalid_pdf_name = "invalid.pdf"

    def test_invalid_request(self):
        invalid_payload = {}
        response = self.client.post(self.url, invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_request(self):
        valid_response = {
            "document": self.valid_pdf_name,
            "start": 0,
            "end": 1,
        }
        response = self.client.post(self.url, valid_response, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

    def test_valid_request_with_learning_goals(self):
        valid_response = {
            "document": self.valid_pdf_name,
            "start": 0,
            "end": 1,
            "learning_goals": ["goal1", "goal2"],
        }
        response = self.client.post(self.url, valid_response, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

    def test_invalid_end_start_index(self):
        invalid_response = {
            "document": self.valid_pdf_name,
            "start": 1,
            "end": 0,
        }
        response = self.client.post(self.url, invalid_response, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class QuizGradingTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = f"{base}quiz/grade/"

    def test_invalid_request(self):
        invalid_payload = {}
        response = self.client.post(self.url, invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_request(self):
        valid_response = {
            "questions": ["question1", "question2"],
            "correct_answers": ["correct1", "correct2"],
            "student_answers": ["answer1", "answer2"],
        }
        response = self.client.post(self.url, valid_response, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)


class FlashcardGenerationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = f"{base}flashcards/create/"
        self.valid_pdf_name = "test.pdf"
        self.invalid_pdf_name = "invalid.pdf"
        self.valid_page_num_start = 0
        self.valid_page_num_end = 1

    def test_invalid_request(self):
        invalid_payload = {}
        response = self.client.post(self.url, invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_request(self):
        valid_response = {
            "document": self.valid_pdf_name,
            "start": self.valid_page_num_start,
            "end": self.valid_page_num_end,
        }
        response = self.client.post(self.url, valid_response, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

    def test_invalid_end_start_index(self):
        invalid_response = {
            "document": self.valid_pdf_name,
            "start": 1,
            "end": 0,
        }
        response = self.client.post(self.url, invalid_response, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CompendiumAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = f"{base}compendium/create/"
        self.valid_document = "test.pdf"
        self.start_page = 1
        self.end_page = 10

    def test_valid_request(self):
        """Test the create_compendium endpoint with a valid request."""
        valid_payload = {
            "document": self.valid_document,
            "start": self.start_page,
            "end": self.end_page,
        }
        response = self.client.post(
            self.url, data=valid_payload, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), dict)  # Ensuring the response is JSON

    def test_invalid_page_range(self):
        """Test the create_compendium endpoint with an invalid page range (start > end)."""
        invalid_payload = {
            "document": self.valid_document,
            "start": 10,
            "end": 1,
        }
        response = self.client.post(
            self.url, data=invalid_payload, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_parameters(self):
        """Test the create_compendium endpoint with missing required parameters."""
        invalid_payloads = [
            {
                "document": self.valid_document,
                "start": self.start_page,
            },  # missing 'end'
            {"document": self.valid_document, "end": self.end_page},  # missing 'start'
            {"start": self.start_page, "end": self.end_page},  # missing 'document'
        ]
        for payload in invalid_payloads:
            response = self.client.post(
                self.url, data=payload, content_type="application/json"
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
