from django.db import models

# Create your models here.


class aluno(models.Model):
    nome = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)  # DEFINIR COMO POSSIVEL NULL
    data_nascimento = models.DateField()


class turma(models.Model):
    curso = models.CharField(max_length=50)
    periodo = models.IntegerField()
    tag = models.CharField(max_lenght=1)


class professor(models.Model):
    nome = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)  # DEFINIR COMO POSSIVEL NULL
    data_nascimento = models.DateField()


class assunto(models.Model):
    nome = models.CharField(max_length=50)


class sentimentos(models.Model):
    nome = models.CharField(max_length=50)
    carater = models.CharField(max_length=10)


class disciplina(models.Model):
    id_professor = models.ForeignKey(professor)
    id_assunto = models.ForeignKey(assunto)
    id_turma = models.ForeignKey(turma)
    carga_horaria = models.IntegerField()


class grade(models.Model):
    id_aluno = models.ForeignKey(aluno)
    id_disciplina = models.ForeignKey(disciplina)


class avaliacao(models.Model):
    id_sentimento = models.ForeignKey(sentimentos)
    id_aluno = models.ForeignKey(aluno)
    id_disciplina = models.ForeignKey(disciplina)  # opção de ser nulo
    comentario = models.CharField(max_lenght=500)
    intensidade = models.IntegerField()
    conhecimento = models.IntegerField()
    data = models.DateField()
