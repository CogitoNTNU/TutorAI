from django.urls import path
from .views import health_check
from flashcards.views import (
    CurriculumUploadView,
    # post_curriculum,
    FlashcardCreationView,
    RAGResponseView,
    QuizCreationView,
    QuizGradingView,
    CompendiumCreationView,
)


urlpatterns = [
    path("health-check/", health_check, name="health-check"),
    path("curriculum/", CurriculumUploadView.as_view(), name="store-curriculum"),
    #    path("curriculum/", CurriculumUploadView.as_view(), name="store-curriculum"),
    path(
        "flashcards/create/", FlashcardCreationView.as_view(), name="create-flashcards"
    ),
    path("search/", RAGResponseView.as_view(), name="create-rag-response"),
    path("quiz/create/", QuizCreationView.as_view(), name="create-quiz"),
    path("quiz/grade/", QuizGradingView.as_view(), name="grade-quiz"),
    path(
        "compendium/create/", CompendiumCreationView.as_view(), name="create-compendium"
    ),
]
