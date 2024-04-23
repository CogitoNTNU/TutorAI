from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status

from flashcards.flashcard_service import generate_quiz, process_flashcards
from flashcards.serializer import CurriculumSerializer, ChatSerializer, QuizSerializer
from .text_to_flashcards import (
    Flashcard,
    generate_flashcards,
    parse_flashcard,
    parse_for_anki,
)
from flashcards.flashcard_service import RagAnswer, process_answer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Flashcard view
get_flashcard_error_response = openapi.Response(
    description="Error generating flashcards",
    examples={"application/json": {"message": "Error generating flashcards"}},
)

get_flashcard_success_response = openapi.Response(
    description="Flashcards generated successfully",
    examples={
        "application/json": [
            {"front": "What is the capital of India?", "back": "New Delhi"}
        ]
    },
)


@swagger_auto_schema(
    method="post",
    operation_description="Generate flashcards from a given text",
    tags=["Flashcards"],
    responses={200: get_flashcard_success_response, 400: get_flashcard_error_response},
)
@api_view(["POST"])
@parser_classes([MultiPartParser])
def create_flashcards(request):
    print(f"[INFO] Request received...", flush=True)
    print(f"request.data: {request.data}", flush=True)
    serializer = CurriculumSerializer(data=request.data)
    if serializer.is_valid():
        uploaded_files: list[InMemoryUploadedFile] = serializer.validated_data.get(
            "curriculum"
        )
        flashcards: list[Flashcard] = []
        for file in uploaded_files:
            flashcards.extend(process_flashcards(file))
        exportable_flashcard = parse_for_anki(flashcards)
        flashcard_dicts = [flashcard.to_dict() for flashcard in flashcards]

        return Response(data=flashcard_dicts, status=200)

    else:
        return Response(serializer.errors, status=400)


@swagger_auto_schema(
    method="get",
    operation_description="Generate flashcards from a predefined text",
    tags=["Flashcards"],
    responses={200: get_flashcard_success_response, 400: get_flashcard_error_response},
)
@api_view(["GET"])
def generate_mock_flashcard(request):
    flashcards = generate_flashcards()
    # flashcards = parse_flashcard(flashcards)

    return Response(flashcards, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_rag_response(request):
    print(f"[INFO] RAG Response Request received... {request}", flush=True)
    # check if request is valid
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        # handle request
        pdf_names = serializer.validated_data.get("documents")
        user_question = serializer.validated_data.get("user_question")
        # Chat history is optional
        chat_history = serializer.validated_data.get("chat_history", [])

        response: RagAnswer = process_answer(pdf_names, user_question, chat_history)

        return Response(response, status=200)

    else:
        print(f"[ERROR] Invalid request: {serializer.errors}", flush=True)
        return Response(serializer.errors, status=400)


@api_view(["POST"])
def create_quiz(request):
    print("[INFO] Create Quiz Request received... {request}")
    serializer = QuizSerializer(data=request.data)
    if serializer.is_valid():
        document = serializer.validated_data.get("document")
        start = serializer.validated_data.get("start")
        end = serializer.validated_data.get("end")
        quiz = generate_quiz(document, start, end)
        response = quiz.to_dict()
        return Response(response, status=200)
    else:
        print(f"[ERROR] Invalid request: {serializer.errors}", flush=True)
        return Response(status=400)
