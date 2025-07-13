from rest_framework import serializers
from .models import Applications

class AppDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applications
        fields = ['id','name','image_path','rating','positive','negative','neutral','appurl']