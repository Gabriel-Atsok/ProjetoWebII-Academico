from django.shortcuts import render

def index(resquest):
    return render(resquest, 'index.html')

def login(resquest):
    return render(resquest, 'login.html')

def registrar(resquest):
    return render(resquest, 'register.html')

def resetsenha(resquest):
    return render(resquest, 'password.html')
