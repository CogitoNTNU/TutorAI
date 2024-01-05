from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
import os

base = "/api/"


class DocumentUploadTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.upload_end_point = f"{base}upload/"
        # Use an existing test PDF file or create a dummy file
        self.valid_pdf = SimpleUploadedFile(
            "test.pdf", b"file_content", content_type="multipart/form-data"
        )
        self.non_valid_file = SimpleUploadedFile(
            "test.txt", b"file_content", content_type="text/plain"
        )

    def tearDown(self):
        # Clean up any created files if necessary
        pass

    def test_no_file(self):
        response = self.client.post(self.upload_end_point, {"pdf": ""})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wrong_file_format(self):
        response = self.client.post(self.upload_end_point, {"pdf": self.non_valid_file})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_pdf(self):
        response = self.client.post(self.upload_end_point, {"pdf": self.valid_pdf})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
