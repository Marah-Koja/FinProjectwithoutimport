import logging
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Applications ,Comment
from .serializers_list import AppListSerializer
from .serializers_details import  AppDetailSerializer
from .serializers_comments import CommentSerializer


# إنشاء logger
logger = logging.getLogger('django')

class AppListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            search_query = request.GET.get('search', '')
            if search_query:
                apps = Applications.objects.filter(name__istartswith=search_query).order_by('-sentiment_score')
            else:
                apps = Applications.objects.all().order_by('-sentiment_score')

            serializer = AppListSerializer(apps, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # سجل الخطأ في ملف log
            logger.error(f"Error fetching applications: {e}")
            # رد على العميل برسالة خطأ
            return Response(
                {"error": "Something went wrong, please try again."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )




class AppDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):  # استقبل pk
        try:
            app = Applications.objects.get(pk=pk)
            serializer = AppDetailSerializer(app)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Applications.DoesNotExist:
            return Response({"error": "App not found."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logger.error(f"Error fetching app detail: {e}")
            return Response({"error": "Something went wrong."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class AppSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            search_query = request.GET.get('search', '')
            apps = Applications.objects.filter(name__istartswith=search_query).order_by('-sentiment_score')
            serializer = AppListSerializer(apps, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error in app search from detail view: {e}")
            return Response({"error": "Something went wrong."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            



# عرض التعليقات
class CommentListView(ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        app_id = self.kwargs['pk']
        return Comment.objects.filter(application_id=app_id).order_by('-created_at')

# إضافة تعليق (محمي)
class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        app_id = self.kwargs['pk']
        serializer.save(user=self.request.user, application_id=app_id)








class AppDownloadView(APIView):
    permission_classes = [IsAuthenticated]  # فقط للمستخدمين المسجلين

    def get(self, request, pk):
        try:
            app = Applications.objects.get(pk=pk)
            return Response({"download_url": app.appurl}, status=status.HTTP_200_OK)
        except Applications.DoesNotExist:
            return Response({"error": "Application not found."}, status=status.HTTP_404_NOT_FOUND)