from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PasswordResetCode
from django.contrib.auth import authenticate
import re

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_email(self, value):
        """تأكد من صيغة الإيميل"""
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise serializers.ValidationError("صيغة البريد الإلكتروني غير صحيحة.")
        return value

    def validate_password(self, value):
        """تأكد من قوة كلمة المرور"""
        if len(value) < 8:
            raise serializers.ValidationError("كلمة المرور يجب أن تكون 8 أحرف على الأقل.")
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError("كلمة المرور يجب أن تحتوي على حرف كبير واحد على الأقل.")
        if not re.search(r"[a-z]", value):
            raise serializers.ValidationError("كلمة المرور يجب أن تحتوي على حرف صغير واحد على الأقل.")
        if not re.search(r"\d", value):
            raise serializers.ValidationError("كلمة المرور يجب أن تحتوي على رقم واحد على الأقل.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise serializers.ValidationError("كلمة المرور يجب أن تحتوي على رمز خاص واحد على الأقل.")
        return value

    def validate(self, attrs):
        """تأكد من تطابق كلمتي المرور"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("كلمتا المرور غير متطابقتين.")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user




class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        
        user = authenticate(username=email, password=password)  # يستخدم EmailBackend
        
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        
        data["user"] = user
        return data










