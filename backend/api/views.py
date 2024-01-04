from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Define your expected request body as a serializer
from rest_framework import serializers


class HelloWorldSerializer(serializers.Serializer):
    name = serializers.CharField(
        required=True, help_text="Name of the person to greet."
    )


@swagger_auto_schema(
    method="post",
    request_body=HelloWorldSerializer,
    operation_description="Post a name and receive a 'Hello' greeting in return.",
)
@api_view(["POST"])
def hello_world(request):
    """
    POST:
    Receive a name in the request body and return a greeting.
    """
    serializer = HelloWorldSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data.get("name")
        return Response(f"Hello {name}")
    else:
        return Response(serializer.errors, status=400)
