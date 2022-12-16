from django.db import models

class Usuario(models.Model):
    matricula=models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)  
    cpf = models.IntegerField()
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
    disciplina_id = models.AutoField(primary_key=True)
    nome_disciplina = models.CharField(max_length=150, blank=True)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)


    def __str__(self):
        return self.nome_disciplina
    
class Turma(models.Model):
    turma_id = models.AutoField(primary_key=True)
    nome_turma = models.CharField(max_length=150)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.nome_turma


