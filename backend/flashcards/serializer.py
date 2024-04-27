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

    # Check if the start index is less than the end index
    def validate(self, data):
        if data["start"] >= data["end"]:
            raise serializers.ValidationError(
                "The start index must be less than the end index"
            )
        return data


class CurriculumSerializer(serializers.Serializer):

    curriculum = serializers.ListField(
        child=serializers.FileField(allow_empty_file=False, use_url=False),
        help_text="The list of files to be processed",
    )
