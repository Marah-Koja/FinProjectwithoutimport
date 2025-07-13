from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers_resetpassword import ResetPasswordSerializer
from .models import PasswordResetCode






class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['code']
        new_password = serializer.validated_data['new_password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Invalid email"}, status=status.HTTP_404_NOT_FOUND)

        try:
            reset_code = PasswordResetCode.objects.filter(user=user, code=code).latest('created_at')
        except PasswordResetCode.DoesNotExist:
            return Response({"error": "Invalid reset code"}, status=status.HTTP_400_BAD_REQUEST)

        if reset_code.is_expired():
            return Response({"error": "Reset code expired"}, status=status.HTTP_400_BAD_REQUEST)

        user.password = make_password(new_password)
        user.save()

        return Response({"message": "Password has been reset successfully"}, status=status.HTTP_200_OK)