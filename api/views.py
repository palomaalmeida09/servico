from django.shortcuts import render
from rest_framework import viewsets 
from .models import User, Todo, Comment, Post
from .serializers import UserSerializer, TodoSerializer, CommentSerializer, PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Permite que o usuário manipule os dados Artista
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    Permite que o usuário manipule os dados de Albuns
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    Permite que o usuário manipule os dados Artista
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    Permite que o usuário manipule os dados Artista
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer