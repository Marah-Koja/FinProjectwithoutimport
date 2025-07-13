from django.urls import path
from .views import AppListView , AppDetailView ,CommentListView, CommentCreateView,AppDownloadView,AppSearchView

urlpatterns = [
    path('', AppListView.as_view(), name='app-list'),
    path('<int:pk>/', AppDetailView.as_view(), name='app-detail'),
     path('<int:pk>/comments/', CommentListView.as_view(), name='comment-list'),
    path('<int:pk>/comments/add/', CommentCreateView.as_view(), name='comment-add'),
    path('<int:pk>/download/', AppDownloadView.as_view(), name='app_download'),
    path('search/', AppSearchView.as_view(), name='app_search_from_details'),

]



    
   