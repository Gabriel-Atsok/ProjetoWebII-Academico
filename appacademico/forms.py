from django import forms
from .models import Usuario, Secretario, Professor, Aluno, Disciplina, Turma

class SecretarioModelForm(forms.ModelForm):
    class Meta:
        model = Secretario
        fields = ['matricula', 'nome', 'cpf', 'telefone', 'email']

class ProfessorModelForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['matricula', 'nome', 'cpf', 'telefone', 'email']

    
class AlunoModelForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['matricula', 'nome', 'cpf', 'telefone', 'email']

class DisciplinaModelForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['disciplina_id', 'matricula']

class TurmaModelForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['turma_id' ,'disciplina_id']

