from django.db import models

# Create your models here.

# create a class for the following tables (comentário criado para o copilot fazer pra mim 😉):
# 1. alunos:
# - id (int)
# - nome (str)

# 2. disciplinas:
# - id (int)
# - nome (str)
# - professor (str)

# 3. notas:
# - id (int)
# - aluno (int)
# - id_disciplina (int)
# - nota (float)


class Aluno(models.Model):
    nome = models.CharField(max_length=100)

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota = models.FloatField()


