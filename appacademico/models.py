from django.db import models


class Usuario(models.Model):
    matricula=models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)  
    cpf=models.CharField(max_length=15)
    telefone=models.IntegerField()
    email=models.EmailField(max_length=50)

    def __str__(self):
        return self.nome
    class Meta:
        abstract = True

class Secretario(Usuario):
    pass
class Professor(Usuario):
    pass
class Aluno(Usuario):
    pass

class Disciplina(models.Model):
    disciplina_id = models.CharField(primary_key=True, max_length=150)
    nome_disciplina = models.CharField(max_length=150, blank=True) 
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_disciplina
    

class Turma(models.Model):
    turma_id = models.AutoField(primary_key=True)
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.turma_id