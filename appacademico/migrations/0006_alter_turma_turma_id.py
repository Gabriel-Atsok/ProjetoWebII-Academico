# Generated by Django 4.1.4 on 2022-12-10 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appacademico', '0005_rename_matricula_do_professor_disciplina_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='turma_id',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
    ]
