from rest_framework import serializers
from .models import YouTubeVideo

class YouTubeVideoSeralizer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideo
        fields = ['title', 'channel']