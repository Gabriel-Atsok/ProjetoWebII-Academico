from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Secretario, Professor, Aluno, Disciplina, Turma
from .forms import SecretarioModelForm, ProfessorModelForm, AlunoModelForm, DisciplinaModelForm, TurmaModelForm


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def registrardocente(request):
    if request.method == "POST":
        docente = ProfessorModelForm(request.POST, request.FILES)
        if docente.is_valid():
            docente.save()
            messages.add_message(request, messages.SUCCESS,'Professor cadastrado com sucesso!')
            return render(request, 'index.html')
    else:
        docente = ProfessorModelForm()
        return render(request, 'register.html', {'docente': docente})


def registrardicente(request):
    if request.method == "POST":
        dicente = AlunoModelForm(request.POST, request.FILES)
        if dicente.is_valid():
            dicente.save()
            messages.add_message(request, messages.SUCCESS,'Aluno cadastrado com sucesso!')
            return render(request, 'index.html')
    else:
        dicente = AlunoModelForm()
        return render(request, 'register.html', {'dicente': dicente})

def registrardisciplina(request):
    if request.method == "POST":
        disciplinas = DisciplinaModelForm(request.POST, request.FILES)
        if disciplinas.is_valid():
            disciplinas.save()
            messages.add_message(request, messages.SUCCESS,'Disciplina cadastrada com sucesso!')
            return render(request, 'index.html')
    else:
        disciplinas = DisciplinaModelForm()
        return render(request, 'register.html', {'disciplinas': disciplinas})

def docentes(request):
    docente = Professor.objects.all()
    return render(request, 'mostrar_todos.html', {'docente': docente})

def dicentes(request):
    dicente = Aluno.objects.all()
    return render(request, 'mostrar_todos.html', {'dicente': dicente})

def disciplinas(request):
    disciplina = Disciplina.objects.all()
    return render(request, 'mostrar_todos.html', {'disciplina': disciplina})

def resetsenha(request):
    return render(request, 'password.html')
