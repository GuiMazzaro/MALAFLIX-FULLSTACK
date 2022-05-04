from django.contrib import admin
from .models import *

class auxCategoria(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class auxFilmes(admin.ModelAdmin):
    list_display = ('id','nome', 'categoriaFK', 'descricao')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10

class auxAssinatura(admin.ModelAdmin):
    list_display = ('id','nomeAssinatura', 'valorAssinatura')
    list_display_links = ('nomeAssinatura',)
    search_fields = ('nomeAssinatura',)
    list_per_page = 10

class auxUsuarios(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'fone', 'dataNascimento', 'idUser', 'plano', 'foto')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10

class auxFavorito(admin.ModelAdmin):
    list_display = ('id','filmeFK', 'usuarioFK')
    list_display_links = ('filmeFK',)
    search_fields = ('filmeFK',)
    list_per_page = 10

admin.site.register(Categoria, auxCategoria)
admin.site.register(Filmes, auxFilmes)
admin.site.register(Assinatura, auxAssinatura)
admin.site.register(Usuarios, auxUsuarios)
admin.site.register(Favorito, auxFavorito)