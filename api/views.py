from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import PostSerializer
from app.models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer