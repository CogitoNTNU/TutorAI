from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from flashcards.flashcard_service import (
    generate_compendium,
    generate_quiz,
    grade_quiz,
    process_flashcards,
    store_curriculum,
    process_answer,
)
from flashcards.text_to_flashcards import parse_for_anki


from flashcards.serializer import (
    CurriculumSerializer,
    ChatSerializer,
    DocumentSerializer,
    QuizStudentAnswer,
)


class CurriculumUploadView(APIView):
    serializer_class = CurriculumSerializer
    parser_classes = [MultiPartParser]

    file_param = openapi.Parameter(
        "curriculum",
        openapi.IN_FORM,
        description="Curriculum files",
        type=openapi.TYPE_FILE,
        required=True,
    )

    @swagger_auto_schema(
        operation_description="Upload curriculum files for processing",
        manual_parameters=[file_param],
        responses={
            200: openapi.Response(description="Files processed successfully"),
            400: openapi.Response(description="Invalid request data"),
        },
        tags=["Curriculum"],
    )
    def post(self, request, *args, **kwargs):
        serializer = CurriculumSerializer(data=request.data)
        if serializer.is_valid():
            uploaded_files: list[InMemoryUploadedFile] = serializer.validated_data.get(
                "curriculum"
            )

            for file in uploaded_files:
                wasUploaded = store_curriculum(file)
                if not wasUploaded:
                    return Response(
                        {"error": f"Failed to upload file: {file.name}"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

            return Response(
                {"message": "Files processed successfully"}, status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardCreationView(GenericAPIView):
    serializer_class = DocumentSerializer

    @swagger_auto_schema(
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
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            file_name = serializer.validated_data.get("document")
            start = serializer.validated_data.get("start")
            end = serializer.validated_data.get("end")

            flashcards = process_flashcards(file_name, start, end)
            exportable_flashcard = parse_for_anki(flashcards)
            flashcard_dicts = [flashcard.to_dict() for flashcard in flashcards]

            response = {
                "flashcards": flashcard_dicts,
                "exportable_flashcards": exportable_flashcard,
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RAGResponseView(GenericAPIView):
    serializer_class = ChatSerializer

    @swagger_auto_schema(
        operation_description="Generate RAG response from given documents and user question",
        request_body=ChatSerializer,
        responses={
            200: openapi.Response(
                description="RAG response generated successfully",
                examples={
                    "application/json": {
                        "answer": "Sample answer",
                        "citations": [
                            {
                                "text": "Sample text",
                                "page_num": 1,
                                "pdf_name": "Sample.pdf",
                            }
                        ],
                    }
                },
            ),
            400: openapi.Response(description="Invalid request data"),
        },
        tags=["RAG"],
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            document_names = serializer.validated_data.get("documents")
            user_question = serializer.validated_data.get("user_question")
            chat_history = serializer.validated_data.get("chat_history", [])

            rag_answer = process_answer(document_names, user_question, chat_history)
            response = rag_answer.to_dict()
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizCreationView(GenericAPIView):
    serializer_class = DocumentSerializer

    @swagger_auto_schema(
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
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            document = serializer.validated_data.get("document")
            start = serializer.validated_data.get("start")
            end = serializer.validated_data.get("end")
            quiz = generate_quiz(document, start, end)
            response = quiz.to_dict()
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizGradingView(GenericAPIView):
    serializer_class = QuizStudentAnswer

    @swagger_auto_schema(
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
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            questions = serializer.validated_data.get("questions")
            student_answers = serializer.validated_data.get("student_answers")
            correct_answers = serializer.validated_data.get("correct_answers")

            graded_answer = grade_quiz(questions, correct_answers, student_answers)
            response = graded_answer.to_dict()
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompendiumCreationView(GenericAPIView):
    serializer_class = DocumentSerializer

    @swagger_auto_schema(
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
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            document = serializer.validated_data.get("document")
            start = serializer.validated_data.get("start")
            end = serializer.validated_data.get("end")
            compendium = generate_compendium(document, start, end)
            response = compendium.to_dict()
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
