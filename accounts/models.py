from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class PasswordResetCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        expiration_time = timedelta(minutes=5)  
        return timezone.now() - self.created_at > expiration_time

    def str(self):
        return f"{self.user.email} - {self.code}"





       


