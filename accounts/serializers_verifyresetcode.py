from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PasswordResetCode







class VerifyResetCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        code = data.get("code")

        if not email or not code:
            raise serializers.ValidationError("Both email and code are required.")

        return data







