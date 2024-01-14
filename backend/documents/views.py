from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Flashcard creation view
create_flashcards_success_response = openapi.Response(
    description="Create flashcards successfully",
    examples={
        "application/json": {
            "message": "Flashcards created successfully",
            "flashcards": [
                {
                    "front": "What is the capital of India?",
                    "back": "New Delhi",
                },
                {
                    "front": "What is the capital of USA?",
                    "back": "Washington DC",
                },
            ],
        }
    },
)

create_flashcards_error_response = openapi.Response(
    description="There was a problem creating flashcards",
    examples={
        "application/json": {"message": "There was a problem creating flashcards"}
    },
)


@swagger_auto_schema(
    method="post",
    operation_description="Login to the application",
    tags=["Document Management"],
    response_description="Returns the list of flashcards created",
    responses={
        200: create_flashcards_success_response,
        400: create_flashcards_error_response,
    },
)
@api_view(["POST"])
def create_flashcards(request):
    print(request.data, flush=True)

    # Check if the uploaded file is a PDF
    if request.content_type != "application/pdf":
        return Response(
            {"message": "The uploaded file is not a PDF"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    pdf_file = request.FILES.get("pdf")

    print(pdf_file, flush=True)
    # Process or save pdf_file as needed
    # ...

    return Response(
        {"message": "PDF uploaded successfully!"}, status=status.HTTP_201_CREATED
    )
