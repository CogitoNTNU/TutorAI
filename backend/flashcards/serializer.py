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


class CurriculumSerializer(serializers.Serializer):

    curriculum = serializers.ListField(
        child=serializers.FileField(allow_empty_file=False, use_url=False),
        help_text="The list of files to be processed",
    )
