from django.test import TestCase, Client
from flashcards.models import Cardset, Flashcard
from users.models import User

# Create your tests here.


base = "/api/"

class GetFlashcardTest(TestCase):

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
        
class testPersistantFlashcard(TestCase):
    
    def setUp(self):
        # This code will run before each test
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.valid_username = "username"

        
    def tearDown(self):
        # This code will run after each test
        self.user.delete()

    def test_persistant_cardset(self):
        self.assertTrue(Cardset.objects.count() == 0)
        
        self.cardset = Cardset.objects.create(name="testcardset", description="testcardset", user=self.user)
        self.assertTrue(Cardset.objects.count() == 1)
        
        self.cardset.delete()
    
    def test_persistant_flashcard(self):
        self.assertTrue(Flashcard.objects.count() == 0)
        
        self.cardset = Cardset.objects.create(name="testcardset", description="testcardset", user=self.user)
        self.card1 = Flashcard.objects.create(front="testfront", back="testback", cardset=self.cardset)
        self.card2 = Flashcard.objects.create(front="testfront2", back="testback2", cardset=self.cardset)
        self.assertTrue(Flashcard.objects.count() == 2)

        self.cardset.delete()
        self.card1.delete()
        self.card2.delete()

    def test_get_flashcards_from_cardset(self):
        self.cardset = Cardset.objects.create(name="testcardset", description="testcardset", user=self.user)
        self.assertTrue(self.cardset.flashcard_set.all().count() == 0)

        self.card1 = Flashcard.objects.create(front="testfront", back="testback", cardset=self.cardset)
        self.card2 = Flashcard.objects.create(front="testfront2", back="testback2", cardset=self.cardset)
        self.assertTrue(self.cardset.flashcard_set.all().count() == 2)
        

        