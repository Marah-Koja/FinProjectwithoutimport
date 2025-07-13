from django.urls import path
from .views import RegisterView,LoginView,LogoutView,ProfileView
from .view_resetpassword import ResetPasswordView
from .view_sendresetcode import SendResetCodeView
from .view_verifyresetcode import VerifyResetCodeView


urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(),name='Login'),
    path('logout/', LogoutView.as_view(),name='Logout'),
       path('send-reset-code/', SendResetCodeView.as_view(), name='send-reset-code'),
    path('verify-reset-code/', VerifyResetCodeView.as_view(), name='verify-reset-code'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('profile/', ProfileView.as_view(),name='profile'),

]




 


 