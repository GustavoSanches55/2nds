from django.shortcuts import render
from django.http import JsonResponse
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

        'Endpoint': '',
        'method': 'GET',
        'body': None,
        'description': 'Returns the homepage'
    },

    {
        'Endpoint': '/alunos/',
        'method': 'GET',
        'body': None,
        'description': 'aluno'
    },
    {
        'Endpoint': '/listarAlunos/',
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
        alunos = aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getAluno(request, pk):
    if request.method == 'GET':
        aluno = aluno.objects.get(id=pk)
        serializer = AlunoSerializer(aluno, many=False)
        return Response(serializer.data)

@api_view(['GET'])
def getTurmas(request):
    if request.method == 'GET':
        return getTurmas(request)

