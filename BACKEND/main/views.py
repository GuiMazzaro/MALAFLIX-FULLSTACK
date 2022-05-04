from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated

class UsuariosAPI(APIView):

    def get(self, request, pk=""):

        if 'nome' in request.GET:
            currentlyName = request.GET['nome']
            usuarios = Usuarios.objects.filter(nome__contains=currentlyName)
            serializer = UsuariosTable(usuarios, many=True)
            return Response(serializer.data)

        elif 'user' in request.GET:
            currentlyUser = request.GET['user']
            usuarios = Usuarios.objects.filter(idUser=currentlyUser)
            serializer = UsuariosTable(usuarios, many=True)
            return Response(serializer.data)

        elif pk == '':
            usuarios = Usuarios.objects.all()
            serializer = UsuariosTable(usuarios, many=True)
            return Response(serializer.data)

        else:
            usuarios = Usuarios.objects.get(id=pk)
            serializer = UsuariosTable(usuarios)
            return Response(serializer.data)

    def post(self, request):
        serializer = UsuariosTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        usuarios = Usuarios.objects.get(id=pk)
        serializer = UsuariosTable(usuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        usuarios = Usuarios.objects.get(id=pk)       
        usuarios.delete()
        return Response({"msg": "Apagado com sucesso"})

class PlanosAPI(APIView):

    def get(self, request, pk=""):
        assinatura = Assinatura.objects.all()
        serializer = AssinaturaTable(assinatura, many=True)
        return Response(serializer.data)

class FilmesAPI(APIView):

    def get(self, request, pk=""):
        filmes = Filmes.objects.all()
        serializer = FilmesTable(filmes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FilmesTable(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})