from django.contrib import admin
from .models import Usuario, Professor, Secretario, Aluno, Disciplina, Turma

# Register your models here.
admin.site.register(Professor)
admin.site.register(Secretario)
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Turma)
