from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

pages = [
    { 'url': 'index', 'name': "Home"},
    { 'url': 'aluno', 'name': "Aluno"},

]

content = {'pages': pages}

def get_route(request):
    return HttpResponse('Home Page')

def aluno(request):
    content['name'] = 'aluno'
    return render(request, 'base/aluno.html', content)
