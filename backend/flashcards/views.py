from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status

from .textToFlashcards import generate_flashcards, parse_flashcard
from .convert_pdf_to_txt import convert_pdf_to_txt

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#Flashcard view
get_flashcard_error_response = openapi.Response(
    description="Error generating flashcards",
    examples={"application/json": {"message": "Error generating flashcards"}},
)

get_flashcard_success_response = openapi.Response(
    description="Flashcards generated successfully",
    examples={"application/json": [{"front": "What is the capital of India?", "back": "New Delhi"}]},
)

@swagger_auto_schema(
    method="post",
    operation_description="Generate flashcards from a given text",
    tags=["Flashcards"],
    responses={200: get_flashcard_error_response, 400: get_flashcard_error_response},
)    

@api_view(["POST"])
def create_flashcards(request):
    # Check if the request has multipart content type
    

    if not request.content_type.startswith('multipart/form-data'):
        return Response(
            {"message": "The uploaded file is not in the correct format"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    pdf_file = request.FILES["pdf"]
    if not pdf_file:
        print("No PDF file uploaded", flush=True)
        return Response(
            {"message": "No PDF file uploaded"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    print("PDF file uploaded successfully", flush=True)

    # Convert the pdf file to text
    text = convert_pdf_to_txt(pdf_file)

    # TODO: split the text into paragraphs before generating flashcards
    text = text[:100]

    flashcards = generate_flashcards(text)
    flashcards = parse_flashcard(flashcards)

    if flashcards == "":
        return Response(
            {"message": "Error generating flashcards"}, status=status.HTTP_400_BAD_REQUEST
        )
    return Response(flashcards, status=status.HTTP_200_OK)