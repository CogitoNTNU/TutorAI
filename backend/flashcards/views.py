from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status

from flashcards.learning_resources import Flashcard, RagAnswer
from flashcards.flashcard_service import (
    generate_compendium,
    generate_quiz,
    grade_quiz,
    process_flashcards,
    store_curriculum,
)
from flashcards.serializer import (
    CurriculumSerializer,
    ChatSerializer,
    DocumentSerializer,
    QuizStudentAnswer,
)
from flashcards.text_to_flashcards import (
    generate_flashcards,
    parse_flashcard,
    parse_for_anki,
)
from flashcards.flashcard_service import process_answer

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


@api_view(["POST"])
@parser_classes([MultiPartParser])
def post_curriculum(request):
    print(f"[INFO] Request received...", flush=True)
    print(f"request.data: {request.data}", flush=True)
    serializer = CurriculumSerializer(data=request.data)
    if serializer.is_valid():
        uploaded_files: list[InMemoryUploadedFile] = serializer.validated_data.get(
            "curriculum"
        )

        for file in uploaded_files:
            wasUploaded = store_curriculum(file)
            # TODO: Handle failure case of store_curriculum
            if not wasUploaded:
                print(f"[ERROR] Failed to upload file: {file}", flush=True)

        return Response(status=200)
    else:
        print(f"[ERROR] Invalid request: {serializer.errors}", flush=True)
        return Response(serializer.errors, status=400)


@swagger_auto_schema(
    method="post",
    operation_description="Generate flashcards from a given text",
    tags=["Flashcards"],
    responses={200: get_flashcard_success_response, 400: get_flashcard_error_response},
)
@api_view(["POST"])
def create_flashcards(request):
    print(f"[INFO] Request received...", flush=True)
    print(f"request.data: {request.data}", flush=True)
    serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        file_name: list[str] = serializer.validated_data.get("document")
        start: int = serializer.validated_data.get("start")
        end: int = serializer.validated_data.get("end")

        # Retrieve the document
        flashcards: list[Flashcard] = process_flashcards(file_name, start, end)

        # Generate flashcards
        exportable_flashcard = parse_for_anki(flashcards)
        flashcard_dicts = [flashcard.to_dict() for flashcard in flashcards]

        response = {
            "flashcards": flashcard_dicts,
            "exportable_flashcards": exportable_flashcard,
        }
        return Response(data=response, status=200)

    else:
        return Response(serializer.errors, status=400)


@api_view(["POST"])
def create_rag_response(request):
    print(f"[INFO] RAG Response Request received... {request}", flush=True)
    # check if request is valid
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        # handle request
        document_names = serializer.validated_data.get("documents")
        user_question = serializer.validated_data.get("user_question")
        # Chat history is optional

        #TEMPORARY FIX
        # document_names.append("Demonstrasjon.pdf")
        document_names.append("Computer.Networking A Top-Down Approach 6th Edition.pdf")
        document_names.append("Book - Clean Architecture - Robert Cecil Martin.pdf")
        document_names.append("Len Bass_ Paul Clements_ Rick Kazman - Software Architecture in Practice, 4th Edition-Addison-Wesley Professional (2021).pdf")
        document_names.append("Compiler.pdf")
        #TEMPORARY FIX

        chat_history = serializer.validated_data.get("chat_history", [])

        rag_answer: RagAnswer = process_answer(
            document_names, user_question, chat_history
        )
        response = rag_answer.to_dict()
        return Response(response, status=200)

    else:
        print(f"[ERROR] Invalid request: {serializer.errors}", flush=True)
        return Response(serializer.errors, status=400)


@api_view(["POST"])
def create_quiz(request):
    print("[INFO] Create Quiz Request received... {request}")
    serializer = DocumentSerializer(data=request.data)
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


@api_view(["POST"])
def grade_quiz_answer(request):
    print("[INFO] Correct Quiz Answer Request received... {request}")
    # TODO: Implement this endpoint
    serializer = QuizStudentAnswer(data=request.data)
    if serializer.is_valid():
        questions = serializer.validated_data.get("questions")
        student_answers = serializer.validated_data.get("student_answers")
        correct_answers = serializer.validated_data.get("correct_answers")

        # Grade the answers
        graded_answer = grade_quiz(questions, correct_answers, student_answers)
        response = graded_answer.to_dict()
        return Response(response, status=200)
    else:
        print(f"[ERROR] Invalid request: {serializer.errors}", flush=True)
        return Response(serializer.errors, status=400)


@api_view(["POST"])
def create_compendium(request):
    print("[INFO] Create Compendium Request received... {request}")
    serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        document = serializer.validated_data.get("document")
        start = serializer.validated_data.get("start")
        end = serializer.validated_data.get("end")

        # Generate the compendium
        compendium = generate_compendium(document, start, end)
        response = compendium.to_dict()
        return Response(response, status=200)
    else:
        print(f"[ERROR] Invalid request: {serializer.errors}", flush=True)
        return Response(status=400)
