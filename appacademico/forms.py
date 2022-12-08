from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome

class Secretario(Usuario):
    pass

class Professor(Usuario):
    pass

class Aluno(Usuario):
    pass

