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
    # list_display = () # grid de visualizações
    # list_filter = ()
    # search_fields = ()
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
    # list_display = () # grid de visualizações
    # list_filter = ()
    # search_fields = ()
    # filter_horizontal = ('aluno',)
    pass

