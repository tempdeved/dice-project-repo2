# Generated by Django 4.1.6 on 2023-03-17 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0005_alter_aluno_created_at_alter_aluno_dat_nasc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='last_name',
            new_name='nome_do_meio',
        ),
        migrations.RenameField(
            model_name='aluno',
            old_name='sobrenome',
            new_name='ultimo_nome',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='nome',
            new_name='nome_completo',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='mes_nascimento',
        ),
        migrations.AddField(
            model_name='aluno',
            name='tel_responsavel_financeiro',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='turma',
            name='flag',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='turma',
            name='semestre',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='bolsista',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='enviar_boleto',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='gerar_taxa',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='status',
            field=models.CharField(blank=True, choices=[('ativo', 'ativo'), ('encerrado', 'encerrado'), ('trancado', 'trancado'), ('jubilado', 'jubilado'), ('cancelado', 'cancelado')], default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='status',
            field=models.CharField(blank=True, choices=[('contratado', 'contratado'), ('contrato encerrado', 'contrato encerrado')], default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='hora_fim',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='hora_inicio',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='min_fim',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='min_inicio',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59')], default='', max_length=2, null=True),
        ),
    ]
