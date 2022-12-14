# Generated by Django 4.1.4 on 2022-12-17 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appacademico', '0003_alter_aluno_turma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appacademico.turma'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='disciplinas',
            field=models.ManyToManyField(blank=True, null=True, related_name='disciplinas', to='appacademico.disciplina'),
        ),
    ]
