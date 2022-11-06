from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_route, name='homepage'),
    path('alunos/get', views.getAluno, name='alunos', kwargs={'pk': 1}),
    path('listarAlunos/', views.getAlunos, name='aluno'),
    
]
