# Generated by Django 4.1.6 on 2023-03-17 03:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0013_remove_turma_tt_turma_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='t',
            field=models.TimeField(default=datetime.time(0, 0), null=True, verbose_name='teste'),
        ),
    ]
