# Generated by Django 4.1.4 on 2022-12-16 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('matricula', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.IntegerField()),
                ('telefone', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('disciplina_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_disciplina', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('matricula', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.IntegerField()),
                ('telefone', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Secretario',
            fields=[
                ('matricula', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.IntegerField()),
                ('telefone', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('turma_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_turma', models.CharField(max_length=150)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appacademico.aluno')),
                ('disciplinas', models.ManyToManyField(to='appacademico.disciplina')),
            ],
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appacademico.professor'),
        ),
    ]
