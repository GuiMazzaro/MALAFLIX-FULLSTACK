from rest_framework import serializers
from .models import *

class UsuariosTable(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Usuarios
        fields = '__all__' 

class FilmesTable(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Filmes
        fields = '__all__'

class CategoriaTable(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Categoria
        fields = '__all__'

class AssinaturaTable(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Assinatura
        fields = '__all__'

class FavoritosTable(serializers.ModelSerializer):

    class Meta:
        many = True
        model = Favorito
        fields = '__all__'