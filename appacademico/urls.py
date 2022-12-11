from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrardocente', views.registrardocente, name='registrardocente'),
    path('registrardiscente', views.registrardiscente, name='registrardiscente'),
    path('registrardisciplina', views.registrardisciplina, name='registrardisciplina'),
    path('registrarturma', views.registrarturma, name='registrarturma'),
    path('docentes', views.docentes, name='docentes'),
    path('discentes', views.discentes, name='discentes'),
    path('disciplinas', views.disciplinas, name='disciplinas'),
    path('turmas', views.turmas, name='turmas'),
    #path('editar_docente/<int:disciplina_id>', views.editar_disciplina, name='editar_disciplina'),
    #path('editar_discente/<int:disciplina_id>', views.editar_disciplina, name='editar_disciplina'),
    path('editar_disciplina/<int:disciplina_id>', views.editar_disciplina, name='editar_disciplina'),
    #path('editar_turma/<int:disciplina_id>', views.editar_disciplina, name='editar_disciplina'),
    path('resetsenha', views.resetsenha, name='resetsenha'),
    path('login', views.login, name='login'),
]