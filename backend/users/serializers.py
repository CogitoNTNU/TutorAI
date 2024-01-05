from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            # "streak_count",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user: User = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            streak_count=0,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(help_text="The username of the user.")
    password = serializers.CharField(
        write_only=True, help_text="The password for the account."
    )
