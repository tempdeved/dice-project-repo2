# Generated by Django 4.1.6 on 2023-03-14 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0003_alter_horario_dia_semana_alter_horario_duracao_min_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='mes_nascimento',
            field=models.IntegerField(blank=True, choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12')], default='', null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='status',
            field=models.CharField(blank=True, choices=[('ativo', 'ativo'), ('encerrado', 'encerrado'), ('trancado', 'trancado'), ('jubilado', 'jubilado')], default='', max_length=100, null=True),
        ),
    ]
