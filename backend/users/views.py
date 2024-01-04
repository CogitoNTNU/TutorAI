from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

# from drf_yasg import openapi

from .serializers import LoginSerializer, RegisterSerializer


@swagger_auto_schema(
    method="post",
    request_body=LoginSerializer,
    operation_description="Login to the application",
    tags=["User Management"],
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


@swagger_auto_schema(
    method="post",
    request_body=RegisterSerializer,
    operation_description="Register a new user to the application. This will create a new user in the database.",
    tags=["User Management"],
)
@api_view(["POST"])
def RegisterUser(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "User registered successfully"}, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
