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


def registrardiscente(request):
    if request.method == "POST":
        discente = AlunoModelForm(request.POST, request.FILES)
        if discente.is_valid():
            discente.save()
            messages.add_message(request, messages.SUCCESS,'Aluno cadastrado com sucesso!')
            return render(request, 'index.html')
    else:
        discente = AlunoModelForm()
        return render(request, 'register.html', {'discente': discente})

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

def discentes(request):
    discente = Aluno.objects.all()
    return render(request, 'mostrar_todos.html', {'discente': discente})

def disciplinas(request):
    disciplina = Disciplina.objects.all()
    return render(request, 'mostrar_todos.html', {'disciplina': disciplina})

def turmas(request):
    turma = Turma.objects.all()
    return render(request, 'mostrar_todos.html', {'turma': turma})

def editar_disciplina(request, disciplina_id):
    disciplinaobject = get_object_or_404(Disciplina, pk=disciplina_id)
    disciplina = DisciplinaModelForm(instance=disciplinaobject)
    if (request.method == "POST"):
        disciplina = DisciplinaModelForm(request.POST, instance=disciplinaobject)
        if (disciplina.is_valid()):
            disciplina.save()
            messages.success(request, f'{disciplinaobject.nome_disciplina.upper()} editado(a) com sucesso!')
            return redirect('disciplinas')
        else:
            return render(request,'editar_todos.html', {'disciplina': disciplina})
    return render(request,'editar_todos.html', {'disciplina': disciplina})

def editar_discente(request, matricula):
    discentenaobject = get_object_or_404(Aluno, pk=matricula)
    discente = AlunoModelForm(instance=discentenaobject)
    if (request.method == "POST"):
        discente = AlunoModelForm(request.POST, instance=discentenaobject)
        if (discente.is_valid()):
            discente.save()
            messages.success(request, f'{discentenaobject.nome.upper()} editado(a) com sucesso!')
            return redirect('discentes')
        else:
            return render(request,'editar_todos.html', {'discente': discente})
    return render(request,'editar_todos.html', {'discente': discente})

def editar_docente(request, matricula):
    docentenaobject = get_object_or_404(Professor, pk=matricula)
    docente = ProfessorModelForm(instance=docentenaobject)
    if (request.method == "POST"):
        docente = ProfessorModelForm(request.POST, instance=docentenaobject)
        if (docente.is_valid()):
            docente.save()
            messages.success(request, f'{docentenaobject.nome.upper()} editado(a) com sucesso!')
            return redirect('docentes')
        else:
            return render(request,'editar_todos.html', {'docente': docente})
    return render(request,'editar_todos.html', {'docente': docente})

def editar_turma(request, turma_id):
    turmaobject = get_object_or_404(Turma, pk=turma_id)
    turma = TurmaModelForm(instance=turmaobject)
    if (request.method == "POST"):
        turma = TurmaModelForm(request.POST, instance=turmaobject)
        if (turma.is_valid()):
            turma.save()
            messages.success(request, f'{turmaobject.turma_id} editado(a) com sucesso!')
            return redirect('turmas')
        else:
            return render(request,'editar_todos.html', {'turma': turma})
    return render(request,'editar_todos.html', {'turma': turma})

def resetsenha(request):
    return render(request, 'password.html')
