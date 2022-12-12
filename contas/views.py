from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = auth.authenticate(request, username=usuario, password=senha)

        if not user:
            messages.error(request, "Usuário ou senha inválidos!")
            return render(request, 'contas/login.html')
        else:
            auth.login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('index')

    return render(request, 'contas/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "Usuário deslogado!")
    return redirect('login')


#@login_required(login_url='login')
def cadastro(request):
    if request.method == "POST":

        usuario = request.POST.get('usuario')
        #nome = request.POST.get('nome')
        #sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')

        if not usuario or not email or not senha1 or not senha2:
            messages.error(request, "Não pode deixar campos em branco!")
            return render(request, 'contas/cadastro.html')

        if len(usuario) < 4:
            messages.info(request, "Nome de usuário muito curto!")
            return render(request, 'contas/cadastro.html')
        try:
            validate_email(email)
        except:
            messages.info(request, "E-mail inválido!")
            return render(request, 'contas/cadastro.html')

        if senha1 != senha2:
            messages.error(request, "Senhas diferentes!")
            return render(request, 'contas/cadastro.html')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, "Usuário já existe.")
            return render(request, 'contas/cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email já existe.")
            return render(request, 'contas/cadastro.html')

        messages.success(request, "Registrado com sucesso!")

        user = User.objects.create_user(username=usuario, email=email,
                                        password=senha1)

        user.save()

        return redirect('login')

    return render(request, 'contas/cadastro.html')


#@login_required(login_url='login')
def edit_cadastro(request):
    if request.method == "POST":
        senha1 = request.POST.get("senha1")
        senha2 = request.POST.get("senha2")

        if not senha1 or not senha2:
            messages.error(request, "Não pode deixar as senhas em branco!")
            return render(request, 'contas/edit_cadastro.html')

        if len(senha1) < 8:
            messages.error(request, "Senha muito curta!")
            return render(request, 'contas/edit_cadastro.html')

        if senha1 != senha2:
            messages.error(request, "Senhas diferentes!")
            return render(request, 'contas/edit_cadastro.html')

        user = get_object_or_404(User, username=request.user)

        user.set_password(senha1)
        user.save()

        messages.success(request, "Senha alterada com sucesso")

        return redirect('login')

    return render(request, 'contas/edit_cadastro.html')
