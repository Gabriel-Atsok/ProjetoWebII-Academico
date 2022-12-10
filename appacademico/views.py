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
        form = ProfessorModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Professor cadastrado com sucesso!')
            return render(request, 'index.html')
    else:
        form = ProfessorModelForm()
        return render(request, 'register.html', {'form': form})


def registrardicente(request):
    if request.method == "POST":
        form = AlunoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Aluno cadastrado com sucesso!')
            return render(request, 'index.html')
    else:
        form = AlunoModelForm()
        return render(request, 'register.html', {'form': form})


def resetsenha(request):
    return render(request, 'password.html')
