from django.shortcuts import render
from rest_framework import viewsets 
from .models import Artista, Album, Musica
from .serializers import ArtistaSerializer, AlbumSerializer, MusicaSerializer

class ArtistaViewSet(viewsets.ModelViewSet):
    """
    Permite que o usuário manipule os dados Artista
    """
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    """
    Permite que o usuário manipule os dados de Albuns
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class MusicaViewSet(viewsets.ModelViewSet):
    """
    Permite que o usuário manipule os dados Artista
    """
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer