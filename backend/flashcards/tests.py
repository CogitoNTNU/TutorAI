from django.test import TestCase, Client

# Create your tests here.


base = "/api/"

class FlashcardTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = base + "generate-mock-flashcard/"
    
    def test_get_flashcards(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_flashcards_format(self):
        response = self.client.get(self.url)
        self.assertEqual(response['Content-Type'], "application/json")
        # Check that response is a list
        self.assertIsInstance(response.json(), list)
        # Check that response items have the correct keys
        self.assertIn("front", response.json()[0])
        self.assertIn("back", response.json()[0])
        