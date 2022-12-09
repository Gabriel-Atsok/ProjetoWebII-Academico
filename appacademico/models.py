from django.db import models


class Usuario(models.Model):
    matricula=models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)  
    cpf=models.CharField(max_length=15)
    telefone=models.IntegerField(max_length=11)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return self.nome

class Secretario(Usuario):
    pass

class Professor(Usuario):
    disciplina_id=models.IntegerField(primary_key=True)
    turma_id=models.CharField(primary_key=True)
    

class Aluno(Usuario):
    disciplina_id=models.IntegerField(primary_key=True)
    turma_id=models.CharField(primary_key=True)
    

class Disciplina:
    nome=models.CharField(max_length=50)
    disciplina_id=models.IntegerField(primary_key=True)
    turma_id=models.CharField(primary_key=True)

class Turma:

    disciplina_id=models.ForeignKey(Professor,Disciplina,on_delete=models.PROTECT)