from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    LoginSerializer,
    RegisterSerializer,
)

# Login view
login_success_response = openapi.Response(
    description="User logged in successfully",
    examples={
        "application/json": {"refresh": "<refresh_token>", "access": "<access_token>"}
    },
)

login_error_response = openapi.Response(
    description="Login failed",
    examples={"application/json": {"message": "Invalid credentials"}},
)


@swagger_auto_schema(
    method="post",
    request_body=LoginSerializer,
    operation_description="Login to the application",
    tags=["User Management"],
    response_description="Returns a JWT token to be used for authentication.",
    responses={200: login_success_response, 401: login_error_response},
)
@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)

    if user is not None:
        # Login successful create a JWT token
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )
    else:
        # Login failed
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


register_success_response = openapi.Response(
    description="User registered successfully",
    examples={"application/json": {"message": "User registered successfully"}},
)

register_error_response = openapi.Response(
    description="Invalid data",
    examples={
        "application/json": {
            "username": ["A user with that username already exists."],
            "email": ["User with this Email already exists."]
            # Include other field errors as appropriate
        }
    },
)


@swagger_auto_schema(
    method="post",
    request_body=RegisterSerializer,
    operation_description="Register a new user to the application. This will create a new user in the database.",
    tags=["User Management"],
    response_description="Returns a message confirming that the user has been registered.",
    responses={201: register_success_response, 400: register_error_response},
)
@api_view(["POST"])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "User registered successfully"}, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
