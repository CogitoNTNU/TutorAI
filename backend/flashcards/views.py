from django.shortcuts import render
from flashcards.textToFlashcards import generate_flashcards, parse_flashcard

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#Flashcard view
get_mock_flashcard_error_response = openapi.Response(
    description="Error generating flashcards",
    examples={"application/json": {"message": "Error generating flashcards"}},
)

get_mock_flashcard_success_response = openapi.Response(
    description="Flashcards generated successfully",
    examples={"application/json": [{"front": "What is the capital of India?", "back": "New Delhi"}]},
)

@swagger_auto_schema(
    method="get",
    operation_description="Generate flashcards from a given text",
    tags=["Flashcards"],
    responses={200: get_mock_flashcard_error_response, 400: get_mock_flashcard_error_response},
)
@api_view(["GET"])
def generate_mock_flashcard(request):
    flashcards = generate_flashcards()
    flashcards = parse_flashcard(flashcards)

    if flashcards == "":
        return Response(
            {"message": "Error generating flashcards"}, status=status.HTTP_400_BAD_REQUEST
        )
    return Response(flashcards, status=status.HTTP_200_OK)
