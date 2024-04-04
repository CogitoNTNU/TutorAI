# serializers.py in your Django app
from rest_framework import serializers


class CurriculumSerializer(serializers.Serializer):
    curriculum = serializers.ListField(
        child=serializers.FileField(allow_empty_file=False, use_url=False),
    )

    def validate_curriculum(self, value):
        # Check minimum number of files
        if len(value) < 1:
            raise serializers.ValidationError("At least one file must be uploaded.")
        return value