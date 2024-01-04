from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

# from drf_yasg import openapi

from .serializers import UserSerializer, LoginSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


@swagger_auto_schema(
    method="post",
    request_body=LoginSerializer,
    operation_description="Login to the application",
)
@api_view(["POST"])
def LoginView(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)

    if user is not None:
        # Login successful
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    else:
        # Login failed
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )
