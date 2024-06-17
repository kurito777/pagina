from rest_framework import serializers
from .models import Author, Manga, TipoSubscripcion, Subscripcion
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'last_name', 'bith_date']

class MangaSerializer(serializers.ModelSerializer):
    author = AuthorSerializer() 

    class Meta:
        model = Manga
        fields = ['idManga', 'title']

class TipoSubscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSubscripcion
        fields = ['id', 'nombre', 'descripcion', 'precio']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class SubscripcionSerializer(serializers.ModelSerializer):
    tipo = TipoSubscripcionSerializer()
    usuario = UserSerializer()

    class Meta:
        model = Subscripcion
        fields = ['id', 'tipo', 'usuario', 'fecha_inicio', 'fecha_fin']