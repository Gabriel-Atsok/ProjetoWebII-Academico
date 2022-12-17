from rolepermissions.roles import AbstractUserRole

class Professor(AbstractUserRole):
    available_permissions = {
        'add_disciplina': True,
        'ver_disciplina': True,
        'ver_turmas': True,
    }

class Aluno(AbstractUserRole):
    available_permissions = {
        'ver_turmas': True,
    }