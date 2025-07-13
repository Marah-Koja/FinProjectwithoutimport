from rest_framework import serializers
from .models import Applications

class AppListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applications
        fields = ['id', 'name','details' ,'image_path', 'rating','sentiment_score']