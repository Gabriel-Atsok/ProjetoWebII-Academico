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
    path('editar_docente/<int:matricula>', views.editar_docente, name='editar_docente'),
    path('editar_discente/<int:matricula>', views.editar_discente, name='editar_discente'),
    path('editar_disciplina/<int:disciplina_id>', views.editar_disciplina, name='editar_disciplina'),
    path('editar_turma/<int:turma_id>', views.editar_turma, name='editar_turma'),
    path('resetsenha', views.resetsenha, name='resetsenha'),
    path('del_discente/<int:matricula>', views.del_discente, name='del_discente'),
    path('del_docente/<int:matricula>', views.del_docente, name='del_docente'),
    path('del_disciplina/<int:disciplina_id>', views.del_disciplina, name='del_disciplina'),
    path('del_turma/<int:turma_id>', views.del_turma, name='del_turma'),
    path('login', views.login, name='login'),
]