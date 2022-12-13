from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.validators import validate_email

from .models import Secretario, Professor, Aluno, Disciplina, Turma
from .forms import SecretarioModelForm, ProfessorModelForm, AlunoModelForm, DisciplinaModelForm, TurmaModelForm


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = auth.authenticate(request, username=usuario, password=senha)

        if not user:
            messages.error(request, 'Usuário ou senha inválidos!')
            return render(request, 'contas/login.html')
        else:
            auth.login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('login')

    return render(request, 'contas/login.html')
    return render(request, 'login.html')


def registrardocente(request):
    docente = ProfessorModelForm()
    if request.method == 'POST':

        matricula = request.POST.get('matricula')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')

        if not nome or not cpf or not telefone or not email:
            messages.error(request, "Não pode deixar campos em branco!")
            return render(request, 'register.html', {'docente': docente})
        
        if len(nome) < 4:
            messages.info(request, "Nome muito curto!")
            return render(request, 'register.html', {'docente': docente})

        if len(cpf) != 11:
            messages.info(request, "Formato de CPF errado!")
            return render(request, 'register.html', {'docente': docente})

        if len(telefone) != 11:
            messages.info(request, "Formato de número incorreto errado!")
            return render(request, 'register.html', {'docente': docente})

        try:
            validate_email(email)
        except:
            messages.info(request, "E-mail inválido!")
            return render(request, 'register.html', {'docente': docente}) 

        else:
            try:
                docente = Professor(matricula=matricula, nome=nome,
                                                cpf=cpf, telefone=telefone,
                                                email=email)
                docente.save()
                docente = Professor.objects.all()
                messages.add_message(request, messages.SUCCESS,
                                        'Professor cadastrado com sucesso!')
                return render(request, 'mostrar_todos.html', {'docente': docente})
            except:
                messages.add_message(request, messages.SUCCESS,
                                        'Erro ao cadastrar!') 
    else:
        return render(request, 'register.html', {'docente': docente})

        
''' def registrardocente(request):
    if request.method == 'POST':
        docente = ProfessorModelForm(request.POST or None, request.FILES or None)
        if docente.is_valid():
            docente.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Professor cadastrado com sucesso!')
            return render(request, 'index.html')
    else:
        docente = ProfessorModelForm()
        return render(request, 'register.html', {'docente': docente}) '''


def registrardiscente(request):
    discente = AlunoModelForm()
    if request.method == 'POST':

        matricula = request.POST.get('matricula')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')

        if not nome or not cpf or not telefone or not email:
            messages.error(request, "Não pode deixar campos em branco!")
            return render(request, 'register.html', {'discente': discente})
        
        if len(nome) < 4:
            messages.info(request, "Nome muito curto!")
            return render(request, 'register.html', {'discente': discente})

        if len(cpf) != 11:
            messages.info(request, "Formato de CPF errado!")
            return render(request, 'register.html', {'discente': discente})

        if len(telefone) != 11:
            messages.info(request, "Formato de número incorreto errado!")
            return render(request, 'register.html', {'discente': discente})

        try:
            validate_email(email)
        except:
            messages.info(request, "E-mail inválido!")
            return render(request, 'register.html', {'discente': discente}) 

        else:
            try:
                discente = Aluno(matricula=matricula, nome=nome,
                                                cpf=cpf, telefone=telefone,
                                                email=email)
                discente.save()
                discente = Aluno.objects.all()
                messages.add_message(request, messages.SUCCESS,
                                        'Aluno cadastrado com sucesso!')
                return render(request, 'mostrar_todos.html', {'discente': discente})
            except:
                messages.add_message(request, messages.SUCCESS,
                                        'Erro ao cadastrar!') 
    else:
        return render(request, 'register.html', {'discente': discente})


def registrardisciplina(request):
    if request.method == 'POST':
        disciplina = DisciplinaModelForm(request.POST or None, request.FILES or None)
        if disciplina.is_valid():
            disciplina.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Disciplina cadastrada com sucesso!')
            return render(request, 'index.html')
    else:
        disciplina = DisciplinaModelForm()
        return render(request, 'register.html', {'disciplina': disciplina})


def registrarturma(request):
    if request.method == 'POST':
        turma = TurmaModelForm(request.POST or None, request.FILES or None)
        if turma.is_valid():
            turma.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Disciplina cadastrada com sucesso!')
            return redirect('turmas')
        else:
            turma = TurmaModelForm()
            return render(request, 'register.html', {'turmas': turma})
    else:
        turma = TurmaModelForm()
        return render(request, 'register.html', {'turmas': turma})


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
    return render(request, 'mostrar_todos.html', {'turmas': turma})


def editar_disciplina(request, disciplina_id):
    disciplinaobject = get_object_or_404(Disciplina, pk=disciplina_id)
    disciplina = DisciplinaModelForm(instance=disciplinaobject)
    if (request.method == 'POST'):
        disciplina = DisciplinaModelForm(
            request.POST, instance=disciplinaobject)
        if (disciplina.is_valid()):
            disciplina.save()
            messages.success(
                request, f'{disciplinaobject.nome_disciplina.upper()} editado(a) com sucesso!')
            return redirect('disciplinas')
        else:
            return render(request, 'editar_todos.html', {'disciplina': disciplina})
    return render(request, 'editar_todos.html', {'disciplina': disciplina})


def editar_discente(request, matricula):
    discentenaobject = get_object_or_404(Aluno, pk=matricula)
    discente = AlunoModelForm(instance=discentenaobject)
    if (request.method == 'POST'):
        discente = AlunoModelForm(request.POST, instance=discentenaobject)
        if (discente.is_valid()):
            discente.save()
            messages.success(
                request, f'{discentenaobject.nome.upper()} editado(a) com sucesso!')
            return redirect('discentes')
        else:
            return render(request, 'editar_todos.html', {'discente': discente})
    return render(request, 'editar_todos.html', {'discente': discente})


def editar_docente(request, matricula):
    docentenaobject = get_object_or_404(Professor, pk=matricula)
    docente = ProfessorModelForm(instance=docentenaobject)
    if (request.method == 'POST'):
        docente = ProfessorModelForm(request.POST, instance=docentenaobject)
        if (docente.is_valid()):
            docente.save()
            messages.success(
                request, f'{docentenaobject.nome.upper()} editado(a) com sucesso!')
            return redirect('docentes')
        else:
            return render(request, 'editar_todos.html', {'docente': docente})
    return render(request, 'editar_todos.html', {'docente': docente})


def editar_turma(request, turma_id):
    turmaobject = get_object_or_404(Turma, pk=turma_id)
    turma = TurmaModelForm(instance=turmaobject)
    if (request.method == 'POST'):
        turma = TurmaModelForm(request.POST, instance=turmaobject)
        if (turma.is_valid()):
            turma.save()
            messages.success(
                request, f'{turmaobject.turma_id} editado(a) com sucesso!')
            return redirect('turmas')
        else:
            return render(request, 'editar_todos.html', {'turmas': turma})
    return render(request, 'editar_todos.html', {'turmas': turma})


def del_discente(request, matricula):
    discente = Aluno.objects.get(matricula=matricula)
    discente.delete()
    messages.success(
        request, f'{discente.nome.upper()} excluído(a) com sucesso!')
    return redirect('discentes')


def del_docente(request, matricula):
    docente = Professor.objects.get(matricula=matricula)
    docente.delete()
    messages.success(
        request, f'{docente.nome.upper()} excluído(a) com sucesso!')
    return redirect('docentes')


def del_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(disciplina_id=disciplina_id)
    disciplina.delete()
    messages.success(
        request, f'{disciplina.nome_disciplina.upper()} excluído(a) com sucesso!')
    return redirect('disciplinas')


def del_turma(request, turma_id):
    turma = Turma.objects.get(turma_id=turma_id)
    turma.delete()
    messages.success(request, f'{turma.turma_id} excluído(a) com sucesso!')
    return redirect('turmas')


def resetsenha(request):
    return render(request, 'password.html')
