from django.shortcuts import render
from rest_framework.views import APIView
from .models import YouTubeVideo
from .serializer import YouTubeVideoSeralizer
from rest_framework.response import Response
# Create your views here.

class YouTubeVideoView(APIView):
    def get(self, request):
        output = [
            {
                "title": output.title,
                "channel": output.channel
            } for output in YouTubeVideo.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = YouTubeVideoSeralizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)