from rest_framework.response import Response
from .models import aluno, turma
from .serializer import AlunoSerializer, TurmaSerializer

def getAlunos(request):
    alunos = aluno.objects.all()
    serializer = AlunoSerializer(alunos, many=True)
    return Response(serializer.data)

def getAluno(request, pk):
    alunos = aluno.objects.get(id=pk)
    serializer = AlunoSerializer(alunos, many=False)
    return Response(serializer.data)

def getTurmas(request):
    turmas = turma.objects.all()
    serializer = TurmaSerializer(turmas, many=True)
    return Response(serializer.data)