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
        fields = ['matricula', 'nome', 'cpf', 'telefone', 'email', 'turma']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 2:
            raise ValueError("Nome no formato errado!")
        else:
            return nome

class DisciplinaModelForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['disciplina_id', 'nome_disciplina', 'professor']

class TurmaModelForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['turma_id' ,'nome_turma', 'disciplinas']

