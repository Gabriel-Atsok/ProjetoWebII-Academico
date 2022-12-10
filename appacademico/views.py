from django.shortcuts import render, redirect, get_object_or_404
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
        disciplina = DisciplinaModelForm(request.POST, request.FILES)
        if disciplina.is_valid():
            disciplina.save()
            messages.add_message(request, messages.SUCCESS,'Disciplina cadastrada com sucesso!')
            return render(request, 'index.html')
    else:
        disciplina = DisciplinaModelForm()
        return render(request, 'register.html', {'disciplina': disciplina})

def registrarturma(request):
    if request.method == "POST":
        turma = TurmaModelForm(request.POST, request.FILES)
        if turma.is_valid():
            turma.save()
            messages.add_message(request, messages.SUCCESS,'Disciplina cadastrada com sucesso!')
            return render(request, 'index.html')
    else:
        turma = TurmaModelForm()
        return render(request, 'register.html', {'turma': turma})

def docentes(request):
    docente = Professor.objects.all()
    return render(request, 'mostrar_todos.html', {'docente': docente})

def dicentes(request):
    dicente = Aluno.objects.all()
    return render(request, 'mostrar_todos.html', {'dicente': dicente})

def disciplinas(request):
    disciplina = Disciplina.objects.all()
    return render(request, 'mostrar_todos.html', {'disciplina': disciplina})

def turmas(request):
    turma = Turma.objects.all()
    return render(request, 'mostrar_todos.html', {'turma': turma})

def editar_disciplina(request, disciplina_id):
    disciplinaobject = get_object_or_404(Disciplina, disciplina_id=disciplina_id)
    print("ATE AQU FOI---------------------------------------------------------------------------------------------------------------------------------------")
    disciplina = DisciplinaModelForm(request.POST or None, request.FILES or None, instance=disciplinaobject)
    if disciplina.is_valid():
        disciplinaobject.save()
        messages.success(request, f'{disciplinaobject.nome_disciplina.upper()} editada com sucesso!')
        return redirect('disciplinas')
#AQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
    return render(request,'editar_todos.html', {'disciplinaobject': disciplinaobject, 'disciplina': disciplina})

def resetsenha(request):
    return render(request, 'password.html')
