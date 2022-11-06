from django.shortcuts import render
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import *
from .serializer import *
from .utils import *

# Create your views here.

@api_view(['GET'])
def get_route(request):
    routes = [
    {

        'name': 'Home',
        'url' : 'index',
        'method': 'GET',
        'body': None,
        'description': 'Página inicial do sistema'
    },

    {
        'name': 'Aluno',
        'url' : 'alunos',
        'method': 'GET',
        'body': None,
        'description': 'Página de alunos do sistema'
    },
    {
        'Endpoint': '/listarAlunos',
        'method': 'GET',
        'body': None,
        'description': 'Lista todos os alunos'
    }

]

    return Response(routes)


# Olha na utils.py, é onde as funções estão.
@api_view(['GET'])
def getAlunos(request):
    if request.method == 'GET':
        return getAlunos(request)

@api_view(['GET'])
def getAluno(request, pk):
    if request.method == 'GET':
        return getAluno(request, pk)

@api_view(['GET'])
def getTurmas(request):
    if request.method == 'GET':
        return getTurmas(request)

