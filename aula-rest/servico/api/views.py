from django.shortcuts import render
from rest_framework import viewsets
from .models import Artista, Album, Musica
from .serializers import ArtistaSerializer, AlbumSerializer, MusicaSerializer

# Create your views here.

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class MusicaViewSet(viewsets.ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer
