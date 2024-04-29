# serializers.py in your Django app
from rest_framework import serializers


class ChatSerializer(serializers.Serializer):
    # The name of the pdf file
    documents = serializers.ListField(
        child=serializers.CharField(
            help_text="The name of the document file",
        ),
        help_text="The names of the documents",
    )

    # The user question
    user_question = serializers.CharField(
        help_text="The user question",
    )

    # The chat history
    chat_history = serializers.ListField(
        child=serializers.DictField(),
        help_text="The chat history",
        required=False,  # Make the field optional
    )

    # Validate the chat history
    def validate_chat_history(self, value):
        if len(value) % 2 != 0:
            raise serializers.ValidationError(
                "The chat history must have an even number of elements"
            )
        for message in value:
            if "role" not in message or "content" not in message:
                raise serializers.ValidationError(
                    "Each message in the chat history must have a role and a content"
                )
        return value


class DocumentSerializer(serializers.Serializer):
    # The name of the pdf file
    document = serializers.CharField(
        help_text="The name of the document file",
    )

    # The start index
    start = serializers.IntegerField(
        help_text="The start index",
    )

    # The end index
    end = serializers.IntegerField(
        help_text="The end index",
    )

    # The learning goals
    learning_goals = serializers.ListField(
        child=serializers.CharField(),
        help_text="The learning goals",
        required=False,  # Make the field optional
    )

    # Check if the start index is less than the end index
    def validate(self, data):
        if data["start"] > data["end"]:
            raise serializers.ValidationError(
                "The start index must be less than the end index"
            )
        return data


class QuizStudentAnswer(serializers.Serializer):
    # Questions: The list of questions
    questions = serializers.ListField(
        child=serializers.CharField(),
        help_text="The list of questions",
    )
    # Answers: The list of answers
    correct_answers = serializers.ListField(
        child=serializers.CharField(),
        help_text="The list of correct answers",
    )
    # Answers: The list of answers
    student_answers = serializers.ListField(
        child=serializers.CharField(),
        help_text="The list of answers",
    )


class CurriculumSerializer(serializers.Serializer):

    curriculum = serializers.ListField(
        child=serializers.FileField(allow_empty_file=False, use_url=False),
        help_text="The list of files to be processed",
    )
