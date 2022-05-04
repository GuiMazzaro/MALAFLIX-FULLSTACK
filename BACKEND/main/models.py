from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

def upload_image_user(instance, filename):
    return f"{filename}"

def upload_image_movie(instance, filename):
    return f"{filename}"

# Create your models here.
class Categoria(models.Model):
    
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Filmes(models.Model):

    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=300)
    categoriaFK = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    capa = models.ImageField(upload_to=upload_image_movie, blank=True, null=True)

    def __str__(self):
        return self.nome

class Assinatura(models.Model):

    nomeAssinatura = models.CharField(max_length=150)
    valorAssinatura = models.FloatField()

    def __str__(self):
        return self.nomeAssinatura

class Usuarios(models.Model):

    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    fone = models.CharField(max_length=30)
    dataNascimento = models.CharField(max_length=100)
    senha = models.CharField(max_length=150)
    plano = models.ForeignKey(Assinatura, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, related_name="usuario", on_delete=models.CASCADE)
    foto = models.ImageField(upload_to=upload_image_user, blank=True, null=True)

    def __str__(self):
        return self.nome

class Favorito(models.Model):

    filmeFK = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    usuarioFK = models.ForeignKey(Usuarios, on_delete=models.CASCADE)