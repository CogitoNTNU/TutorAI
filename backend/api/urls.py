from django.urls import path


from .views import health_check
from flashcards.views import (
    create_compendium,
    create_flashcards,
    create_quiz,
    grade_quiz_answer,
    create_rag_response,
    post_curriculum,
)

urlpatterns = [
    # path("create-user/", register_user, name="create-user"),
    # path("login/", login, name="login"),
    path("health-check/", health_check, name="Health_check"),
    path("store-curriculum/", post_curriculum, name="store-curriculum"),
    path("create-flashcards/", create_flashcards, name="create-flashcards"),
    path("search/", create_rag_response, name="create-rag-response"),
    path("quiz/", create_quiz, name="create-quiz"), 
    path("graded-quiz/", grade_quiz_answer, name="create-graded-quiz")
    path("compendium/", create_compendium, name="create-compendium"),
]
