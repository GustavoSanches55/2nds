from django.shortcuts import render
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import *
from .serializer import *
#from .utils import *

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

]

    return Response(routes)






