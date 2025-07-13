from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
import random
from .models import PasswordResetCode
from django.core.mail import send_mail
from .serializers_forgetpassword import ForgotPasswordSerializer






class SendResetCodeView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        user = User.objects.get(email=email)
        code = str(random.randint(1000, 9999))

        PasswordResetCode.objects.create(user=user, code=code)

        send_mail(
            subject='Your Password Reset Code',
            message=f'Your password reset code is: {code}',
            from_email=None,  # يستخدم DEFAULT_FROM_EMAIL في settings
            recipient_list=[email],
            fail_silently=False,
        )

        return Response({'message': 'Reset code sent to your email'}, status=status.HTTP_200_OK)
