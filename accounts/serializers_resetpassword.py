from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PasswordResetCode





class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()
    new_password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        if not confirm_password:
            raise serializers.ValidationError("You must confirm the password.")

        if new_password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        return data