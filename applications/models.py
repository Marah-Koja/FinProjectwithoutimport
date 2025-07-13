from django.db import models
from django.contrib.auth.models import User

class Applications(models.Model):
    name = models.CharField(max_length=100)
    app_id = models.CharField(max_length=100, unique=True)
    details = models.TextField(blank=True, null=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)
    appurl = models.URLField(max_length=255, blank=True, null=True)
    def save(self, *args, **kwargs):
         if not self.appurl:
            self.appurl = f"https://play.google.com/store/apps/details?id={self.package_id}"
         super().save(*args, **kwargs)

    rating = models.FloatField(default=0.0)
    positive = models.FloatField(default=0.0)
    negative = models.FloatField(default=0.0)
    neutral = models.FloatField(default=0.0)
    sentiment_score = models.FloatField(default=0.0)
    total_comments=models.IntegerField(default=0.0)

    def str(self):
        return self.name




class Comment(models.Model):
    application = models.ForeignKey('Applications', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"تعليق بواسطة {self.user.username} على {self.application.name}"