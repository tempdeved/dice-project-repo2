from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    # list_display = () # grid de visualizações
    # list_filter = ()
    # search_fields = ()
    # filter_horizontal = ('aluno',)
    pass

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'id',
        'nome',
        'status',
        'dat_nasc',
        'bairro',
        'nome_mae',
        'nome_pai',
        'foto',
    ) # grid de visualizações
    # list_filter = ()
    search_fields = (
        'id',
        'nome',
        'status',
        'dat_nasc',
        'bairro',
        'nome_mae',
        'nome_pai',
    )
    # filter_horizontal = ('aluno',)
    pass


@admin.register(models.Horario)
class HorarioAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    # list_display = () # grid de visualizações
    # list_filter = ()
    # search_fields = ()
    # filter_horizontal = ('aluno',)
    pass

@admin.register(models.Turma)
class TurmaAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    # list_display = () # grid de visualizações
    # list_filter = ()
    # search_fields = ()
    filter_horizontal = ('aluno',)
    pass

@admin.register(models.HistoricoAluno)
class HistoricoAlunoAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'turma',
        'aluno',
        'frequencia_pct',
        'media_final',

    ) # grid de visualizações
    # list_filter = ()
    search_fields = (
        'turma',
        'aluno',
    )

    # filter_horizontal = ('aluno',)
    pass

