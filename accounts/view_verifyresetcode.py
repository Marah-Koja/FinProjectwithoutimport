from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.utils import timezone
from .models import PasswordResetCode
from .serializers_verifyresetcode import VerifyResetCodeSerializer


class VerifyResetCodeView(APIView):
    def post(self, request):
        serializer = VerifyResetCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['code']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid email'}, status=status.HTTP_404_NOT_FOUND)

        # فينا نفلتر الكود ونتأكد من تاريخه بعدين
        reset_codes = PasswordResetCode.objects.filter(user=user, code=code)

        if not reset_codes.exists():
            return Response({'error': 'Invalid code'}, status=status.HTTP_400_BAD_REQUEST)

        # نأخذ أحدث كود مطابق
        reset_code = reset_codes.latest('created_at')

        if reset_code.is_expired():
            return Response({'error': 'Code has expired'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Code verified successfully'}, status=status.HTTP_200_OK)