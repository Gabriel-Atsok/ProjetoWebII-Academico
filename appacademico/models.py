from django.db import models

class Usuario(models.Model):
    matricula= models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)  
    cpf = models.IntegerField()
    telefone=models.IntegerField()
    email=models.EmailField(max_length=50)

    def __str__(self):
        return self.nome
    class Meta:
        abstract = True
    
class Professor(Usuario):
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
    disciplinas = models.ManyToManyField(Disciplina, related_name='disciplinas')

    def __str__(self):
        return self.nome_turma


class Secretario(Usuario):
    pass

class Aluno(Usuario):
    turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
    pass

    


