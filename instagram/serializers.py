# serializers.py
from rest_framework import serializers
from .models import InstagramPost

class InstagramPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramPost
        fields = ['id', 'media_type', 'image', 'video', 'caption', 'profile']
