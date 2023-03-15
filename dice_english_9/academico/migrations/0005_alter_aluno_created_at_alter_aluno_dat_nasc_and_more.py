# Generated by Django 4.1.6 on 2023-03-15 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0004_alter_aluno_mes_nascimento_alter_aluno_sexo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='dat_nasc',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='inicio',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='retorno',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='dat_nasc',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='historicoaluno',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='fim',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='inicio',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='status',
            field=models.CharField(blank=True, choices=[('ativo', 'ativo'), ('encerrada', 'encerrada')], default='', max_length=100, null=True),
        ),
    ]
