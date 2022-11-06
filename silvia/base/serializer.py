from rest_framework.serializers import ModelSerializer
from base.models import *

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = aluno
        fields = '__all__'

class TurmaSerializer(ModelSerializer):
    class Meta:
        model = turma
        fields = '__all__'

class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = professor
        fields = '__all__'

class AssuntoSerializer(ModelSerializer):
    class Meta:
        model = assunto
        fields = '__all__'

class SentimentosSerializer(ModelSerializer):
    class Meta:
        model = sentimentos
        fields = '__all__'
    
class DisciplinaSerializer(ModelSerializer):
    class Meta:
        model = disciplina
        fields = '__all__'

class GradeSerializer(ModelSerializer):
    class Meta:
        model = grade
        fields = '__all__'

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = avaliacao
        fields = '__all__'
    
