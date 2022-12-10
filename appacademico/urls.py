from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrardocente', views.registrardocente, name='registrardocente'),
    path('registrardicente', views.registrardicente, name='registrardicente'),
    path('registrardisciplina', views.registrardisciplina, name='registrardisciplina'),
    path('registrarturma', views.registrarturma, name='registrarturma'),
    path('docentes', views.docentes, name='docentes'),
    path('dicentes', views.dicentes, name='dicentes'),
    path('disciplinas', views.disciplinas, name='disciplinas'),
    path('turmas', views.turmas, name='turmas'),
    path('editar_disciplina', views.editar_disciplina, name='editar_disciplina'),
    path('resetsenha', views.resetsenha, name='resetsenha'),
    path('login', views.login, name='login'),
]