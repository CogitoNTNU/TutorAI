from django.core.files.uploadedfile import InMemoryUploadedFile
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
from flashcards.text_to_flashcards import parse_for_anki
from flashcards.flashcard_service import process_answer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Define file upload parameter
file_param = openapi.Parameter(
    "curriculum",
    openapi.IN_FORM,
    description="Curriculum files",
    type=openapi.TYPE_FILE,
    required=True,
)


@swagger_auto_schema(
    method="post",
    operation_description="Upload curriculum files for processing",
    manual_parameters=[file_param],
    responses={
        200: openapi.Response(description="Files processed successfully"),
        400: openapi.Response(description="Invalid request data"),
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
                return Response(
                    {"error": f"Failed to upload file: {file.name}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(
            {"message": "Files processed successfully"}, status=status.HTTP_200_OK
        )
    else:
        print(f"[ERROR] Invalid request: {serializer.errors}", flush=True)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="post",
    operation_description="Generate flashcards from a given document",
    request_body=DocumentSerializer,
    responses={
        200: openapi.Response(
            description="Flashcards generated successfully",
            examples={
                "application/json": {
                    "flashcards": [
                        {
                            "front": "Sample question?",
                            "back": "Sample answer",
                            "pdf_name": "Sample.pdf",
                            "page_num": 1,
                        }
                    ],
                    "exportable_flashcards": "Sample question?: Sample answer\n",
                }
            },
        ),
        400: openapi.Response(description="Invalid request data"),
    },
    tags=["Flashcards"],
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
        return Response(data=response, status=status.HTTP_200_OK)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="post",
    operation_description="Generate RAG response from given documents and user question",
    request_body=ChatSerializer,
    responses={
        200: openapi.Response(
            description="RAG response generated successfully",
            examples={
                "application/json": {
                    "answer": "Sample answer",
                    "citations": [
                        {"text": "Sample text", "page_num": 1, "pdf_name": "Sample.pdf"}
                    ],
                }
            },
        ),
        400: openapi.Response(description="Invalid request data"),
    },
    tags=["RAG"],
)
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

        # TEMPORARY FIX
        # document_names.append("Demonstrasjon.pdf")
        document_names.append("Compiler.pdf")
        # TEMPORARY FIX

        chat_history = serializer.validated_data.get("chat_history", [])

        rag_answer: RagAnswer = process_answer(
            document_names, user_question, chat_history
        )
        response = rag_answer.to_dict()
        return Response(response, status=status.HTTP_200_OK)

    else:
        print(f"[ERROR] Invalid request: {serializer.errors}", flush=True)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="post",
    operation_description="Create a quiz from a given document",
    request_body=DocumentSerializer,
    responses={
        200: openapi.Response(
            description="Quiz created successfully",
            examples={
                "application/json": {
                    "document": "Sample.pdf",
                    "start": 1,
                    "end": 10,
                    "questions": [
                        {"question": "Sample question?", "answer": "Sample answer"}
                    ],
                }
            },
        ),
        400: openapi.Response(description="Invalid request data"),
    },
    tags=["Quiz"],
)
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
        return Response(response, status=status.HTTP_200_OK)
    else:
        print(f"[ERROR] Invalid request: {serializer.errors}", flush=True)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="post",
    operation_description="Grade the student's quiz answers",
    request_body=QuizStudentAnswer,
    responses={
        200: openapi.Response(
            description="Quiz graded successfully",
            examples={
                "application/json": {
                    "answers_was_correct": [True, False, True],
                    "feedback": ["Correct", "Incorrect", "Correct"],
                }
            },
        ),
        400: openapi.Response(description="Invalid request data"),
    },
    tags=["Quiz"],
)
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
        return Response(response, status=status.HTTP_200_OK)
    else:
        print(f"[ERROR] Invalid request: {serializer.errors}", flush=True)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="post",
    operation_description="Create a compendium from a given document",
    request_body=DocumentSerializer,
    responses={
        200: openapi.Response(
            description="Compendium created successfully",
            examples={
                "application/json": {
                    "document": "Sample.pdf",
                    "start": 1,
                    "end": 10,
                    "key_concepts": ["Concept 1", "Concept 2"],
                    "summary": "This is a summary of the document.",
                }
            },
        ),
        400: openapi.Response(description="Invalid request data"),
    },
    tags=["Compendium"],
)
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
        return Response(response, status=status.HTTP_200_OK)
    else:
        print(f"[ERROR] Invalid request: {serializer.errors}", flush=True)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
