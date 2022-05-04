from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("usuarios/", UsuariosAPI.as_view(), name="usuarios"),
    path("usuarios/<int:pk>/", UsuariosAPI.as_view(), name="usuariosParametros"),
    path("planos/", PlanosAPI.as_view(), name="planos"),
    path("planos/<int:pk>/", PlanosAPI.as_view(), name="planosParametros"),
    path("filmes/", FilmesAPI.as_view(), name="filmes"),
    path("filmes/<int:pk>/", FilmesAPI.as_view(), name="filmesParametros"),
]