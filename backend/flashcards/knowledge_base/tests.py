from django.test import TestCase
from flashcards.knowledge_base.embeddings import cosine_similarity
from flashcards.knowledge_base.embeddings import OpenAIEmbedding
from flashcards.knowledge_base.db_interface import MongoDB
from config import Config


class MongoDBTest(TestCase):
    def setUp(self):
        # Initialize MongoDB connection
        self.mongo = MongoDB(uri=Config().MONGODB_TEST_URI)

        self.curriculum = {"pdf1":"Antonio López de Santa Anna var en meksikansk politiker og general. Fra slutten av 1820-årene og frem til 1855 dominerte han Mexicos politiske liv, og var president seks ganger. Han var en ytterst fargerik personlighet uten noen politisk filosofi, men meget populær blant folket.",
                           "pdf2":"I 1829 gjorde spanske tropper et mislykket forsøk på å gjenerobre Mexico. Santa Annas seier mot invasjonsstyrken i Tampico ga ham anerkjennelse som nasjonalist og militærstrateg, et omdømme han nøt godt av de neste 25 årene. Gjennom karrieren var Santa Anna en typisk caudillo som vekslet mellom politisk og militær makt, i en tid da militærmakt var nøkkelen til politisk kontroll.",
                           "pdf3":"I 1833 kom han til makten som føderalist og motstander av den romersk-katolske kirken; i praksis etablerte han en sentralisert stat. Han forble ved presidentmakten til 1836, da han ledet meksikanske tropper inn i Texas for å dempe Texasrevolusjonen. Her ble han tatt til fange av Sam Houston, og ble tvunget til å anerkjenne den nye Republikken Texas."}

        for key in self.curriculum.keys():
            self.mongo.post_curriculum(self.curriculum[key], 1, key, OpenAIEmbedding().get_embedding(self.curriculum[key]))
        
    def test_get_curriculum(self):
        # Test getting curriculum
        curriculum = self.mongo.get_curriculum(OpenAIEmbedding().get_embedding(self.curriculum["pdf1"]))
        self.assertEqual(len(curriculum), 1)
        self.assertEqual(curriculum[0].text, self.curriculum["pdf1"])
        self.assertEqual(curriculum[0].page_num, 1)
        self.assertEqual(curriculum[0].pdf_name, "pdf1")

        # Test getting curriculum using query
        curriculum = self.mongo.get_curriculum(OpenAIEmbedding().get_embedding("Den romersk-katolske kirken var ikke stor i Texas under revolusjonen. Sam Houston var personlig en protestant"))
        self.assertEqual(len(curriculum), 1)
        self.assertEqual(curriculum[0].text, self.curriculum["pdf3"])
        self.assertEqual(curriculum[0].page_num, 1)
        self.assertEqual(curriculum[0].pdf_name, "pdf3")

    def test_delete_pdf_pages(self):
        # Test deleting curriculum entries with specific PDF name
        self.assertTrue(self.mongo.delete_pdf_pages("pdf1"))

        # Check if curriculum entries with pdfName="pdf1" were deleted
        self.assertRaises(ValueError("No documents found"),self.mongo.get_curriculum(OpenAIEmbedding().get_embedding(self.curriculum["pdf1"])))

    def tearDown(self):
        # Clean up test data
        self.mongo.delete_all_curriculum()