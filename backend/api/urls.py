from django.urls import path

# from users.views import login, register_user
from flashcards.views import create_flashcards, generate_mock_flashcard

urlpatterns = [
    # path("create-user/", register_user, name="create-user"),
    # path("login/", login, name="login"),
    path("generate-mock-flashcard/", generate_mock_flashcard, name="generate-mock-flashcards"),
    path("create-flashcards/", create_flashcards, name="create-flashcards"),
    path("generate-mock-flashcard/", generate_mock_flashcard, name="generate-mock-flashcard"),
]
