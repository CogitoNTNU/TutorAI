from django.test import TestCase, Client
from rest_framework import status
import json
from users.models import User

# Create your tests here.

base = "/api/"


class UserCreationTests(TestCase):
    def setUp(self):
        # This code will run before each test
        self.register_end_point = f"{base}create-user/"
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.valid_username = "username"

    def tearDown(self):
        # This code will run after each test
        self.user.delete()

    def test_valid_nonexistent_user(self):
        client = Client()
        # Create user
        request_body: dict = {
            "username": self.valid_username,
            "password": "test",
            "email": "test@test.com",
            "first_name": "simon",
            "last_name": "sandvik",
            "streak_count": 1,
        }
        response = client.post(self.register_end_point, request_body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Tear down just for this test
        User.objects.get(username=self.valid_username).delete()

    def test_username_blank(self):
        client = Client()
        # Create user
        string_blank: str = ""
        request_body: dict = {
            "username": string_blank,
            "password": "test",
            "email": "test@test.com",
            "first_name": "simon",
            "last_name": "sandvik",
            "streak_count": 1,
        }
        response = client.post(self.register_end_point, request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_username_too_long(self):
        client = Client()
        # Create user
        string_long: str = "a" * 151
        request_body: dict = {
            "username": string_long,
            "password": "test",
            "email": "test@test.com",
            "first_name": "simon",
            "last_name": "sandvik",
            "streak_count": 1,
        }
        response = client.post(self.register_end_point, request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_already_existing_user(self):
        client = Client()
        request_body = {
            "username": self.user.username,
            "password": "test",
            "email": "test@test.com",
            "first_name": "simon",
            "last_name": "sandvik",
            "streak_count": 1,
        }

        response = client.post(self.register_end_point, request_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_email(self):
        client = Client()
        valid_email: str = "test@test.com"
        request_body = {
            "username": "username",
            "password": "test",
            "email": valid_email,
            "first_name": "simon",
            "last_name": "sandvik",
            "streak_count": 1,
        }

        response = client.post(self.register_end_point, request_body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginTests(TestCase):
    def setUp(self):
        self.login_end_point = f"{base}login/"
        # This code will run before each test
        self.user_pasword = "a12345"
        self.user = User.objects.create_user(
            username="logintestuser", password=self.user_pasword
        )
        self.different_user_password = "differentuserpassword"
        self.different_user = User.objects.create_user(
            username="differentuser", password=self.different_user_password
        )

    def tearDown(self):
        # This code will run after each test
        self.user.delete()
        self.different_user.delete()

    def test_invalid_login_attempt_with_empty_fields(self):
        client = Client()
        # Create user to use
        invalid_username: str = ""
        invalid_password: str = ""
        request_body: dict = {
            "username": invalid_username,
            "password": invalid_password,
        }

        response = client.post(self.login_end_point, request_body)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_login_attempt_to_non_existing_valid_user(self):
        client = Client()
        # Create user to use
        invalid_username: str = "SimonSandvikLeeErKulOgFlott1"
        invalid_password: str = "P21241!,.$"
        request_body: dict = {
            "username": invalid_username,
            "password": invalid_password,
        }

        response = client.post(self.login_end_point, request_body)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_login_on_existing_user_with_capital_letters_in_username(self):
        client = Client()
        request_body = {
            "username": str(self.user.username).upper(),
            "password": self.user_pasword,
        }

        response = client.post(self.login_end_point, request_body)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_login_on_existing_user_with_capital_letters_in_password(self):
        client = Client()
        request_body = {
            "username": self.user.username,
            "password": str(self.user_pasword).upper(),
        }

        response = client.post(self.login_end_point, request_body)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_login_on_existing_user(self):
        client = Client()
        request_body = {"username": self.user.username, "password": self.user_pasword}

        response = client.post(self.login_end_point, request_body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_correct_username_valid_on_existing_user(self):
        client = Client()
        request_body = {"username": self.user.username, "password": "WRONG-PASSWORD"}

        response = client.post(self.login_end_point, request_body)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_correct_pass_valid_on_existing_user(self):
        client = Client()
        request_body = {"username": "WRONG-PASSWORD", "password": self.user_pasword}

        response = client.post(self.login_end_point, request_body)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_login_gets_jwt_tokens(self):
        client = Client()
        request_body = {"username": self.user.username, "password": self.user_pasword}

        response = client.post(self.login_end_point, request_body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("refresh" in response.data)
        self.assertTrue("access" in response.data)
        access = response.data.get("access")
        refresh = response.data.get("refresh")
        self.assertNotEqual(access, refresh)

    def test_valid_logins_gets_different_jwt_tokens(self):
        client = Client()
        request_body1 = {"username": self.user.username, "password": self.user_pasword}
        request_body2 = {
            "username": self.different_user.username,
            "password": self.different_user_password,
        }
        response1 = client.post(self.login_end_point, request_body1)
        response2 = client.post(self.login_end_point, request_body2)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

        access1 = response1.data.get("access")
        refresh1 = response1.data.get("refresh")
        access2 = response2.data.get("access")
        refresh2 = response2.data.get("refresh")
        self.assertNotEqual(access1, access2)
        self.assertNotEqual(refresh1, refresh2)
