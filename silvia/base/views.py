from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import *
from .serializer import *
from .utils import *
from .graph_gen import *

# Create your views here.
#We need an request to run a script to generate graphs, so we need to create a view and a url for it in order to acess it in the react frontend


def graph_make(request):    
    random_words = create_random_words() #Aqui nos gostariamos de parsear com um modelo de nlp as avaliacoes para remoçao de stop words e entao usar essas palavras, porem fizemos aleatorio para demonstrar devido a falta de tempo
    df_final, disciplina, professor = create_df(random_words)
    create_general_graph(df_final, disciplina, professor)
    for teacher_id in df_final.id_professor_id.unique():
        create_teacher_graph(df_final, disciplina, professor, teacher_id)
    return HttpResponse("Graphs created")




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
        al = aluno.objects.get(id=pk)
        serializer = AlunoSerializer(al, many=False)
        return Response(serializer.data)
        

@api_view(['GET'])
def getTurmas(request):
    if request.method == 'GET':
        turmas = turma.objects.all()
        serializer = TurmaSerializer(turmas, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getTurma(request, pk):
    if request.method == 'GET':
        tu = turma.objects.get(id=pk)
        serializer = TurmaSerializer(tu , many=False)
        return Response(serializer.data)

@api_view(['GET'])
def getProfessores(request):
    if request.method == 'GET':
        professores = professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getProfessor(request, pk):
    if request.method == 'GET':
        pr = professor.objects.get(id=pk)
        serializer = ProfessorSerializer(pr , many=False)
        return Response(serializer.data)


@api_view(['GET'])
def getAssuntos(request):
    if request.method == 'GET':
        assuntos = assunto.objects.all()
        serializer = AssuntoSerializer(assuntos, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getAssunto(request, pk):
    if request.method == 'GET':
        ass  = assunto.objects.get(id=pk)
        serializer = AssuntoSerializer(ass , many=False)
        return Response(serializer.data)

@api_view(['GET'])
def getSentimentos(request):
    if request.method == 'GET':
        sentimentos = sentimentos.objects.all()
        serializer = SentimentosSerializer(sentimentos, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getSentimento(request, pk):
    if request.method == 'GET':
        se = sentimentos.objects.get(id=pk)
        serializer = SentimentosSerializer(se , many=False)
        return Response(serializer.data)

@api_view(['GET'])
def getDisciplinas(request):
    if request.method == 'GET':
        disciplinas = disciplina.objects.all()
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getDisciplina(request, pk):
    if request.method == 'GET':
        di  = disciplina.objects.get(id=pk)
        serializer = DisciplinaSerializer(di , many=False)
        return Response(serializer.data)

@api_view(['GET'])
def getAvaliacoes(request):
    if request.method == 'GET':
        avaliacoes = avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getAvaliacao(request, pk):
    if request.method == 'GET':
        av = avaliacao.objects.get(id=pk)
        serializer = AvaliacaoSerializer(av , many=False)
        return Response(serializer.data)


@api_view(['POST', 'DELETE'])
def constructAluno(request):
    if request.method == 'POST':
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        aluno.objects.all().delete()
        return Response('Alunos deletados com sucesso')

@api_view(['POST', 'DELETE'])
def constructTurma(request):
    if request.method == 'POST':
        serializer = TurmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        turma.objects.all().delete()
        return Response('Turmas deletadas com sucesso')

@api_view(['POST', 'DELETE'])
def constructProfessor(request):
    if request.method == 'POST':
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        professor.objects.all().delete()
        return Response('Professores deletados com sucesso')

@api_view(['POST', 'DELETE'])
def constructAssunto(request):
    if request.method == 'POST':
        serializer = AssuntoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        assunto.objects.all().delete()
        return Response('Assuntos deletados com sucesso')
    
@api_view(['POST', 'DELETE'])
def constructSentimento(request):
    if request.method == 'POST':
        serializer = SentimentosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        sentimentos.objects.all().delete()
        return Response('Sentimentos deletados com sucesso')

@api_view(['POST', 'DELETE'])
def constructDisciplina(request):
    if request.method == 'POST':
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        disciplina.objects.all().delete()
        return Response('Disciplinas deletadas com sucesso')

@api_view(['POST', 'DELETE'])
def constructAvaliacao(request):
    if request.method == 'POST':
        serializer = AvaliacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        avaliacao.objects.all().delete()
        return Response('Avaliações deletadas com sucesso')
        

    

