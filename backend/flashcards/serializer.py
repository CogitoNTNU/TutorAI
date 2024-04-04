# serializers.py in your Django app
from rest_framework import serializers


class CurriculumSerializer(serializers.Serializer):
    
    serializers.FileField(allow_empty_file=False, use_url=False)
