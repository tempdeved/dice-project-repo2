from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'nome',
        'funcao',
        'status',
        'telefone1',
        'telefone2',
        'email',
    ) # grid de visualizações
    # list_filter = ()
    # search_fields = ()
    # filter_horizontal = ('aluno',)
    pass

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'id',
        'full_name',
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
    list_display = (
        'dia_semana',
        'v_hora',
    ) # grid de visualizações
    # list_filter = ()
    # search_fields = ()
    # filter_horizontal = ('aluno',)
    @admin.display(description='Hora')
    def v_hora(self, obj):
        return f'{obj.hora_inicio}:{obj.min_inicio}-' \
           f'{obj.hora_fim}:{obj.min_fim}'
    pass

@admin.register(models.Turma)
class TurmaAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'v_created_at',
        'horario',
        'status',
    ) # grid de visualizações
    list_filter = (
        'created_at',
        'horario',
        'status',
    )
    # search_fields = ()
    filter_horizontal = ('aluno',)

    @admin.display(description='Turma')
    def v_created_at(self, obj):
        return f'{obj.created_at.year}-{obj.created_at.month}'

    pass

@admin.register(models.HistoricoAluno)
class HistoricoAlunoAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'v_created_at',
        'v_week_at',
        'aluno',
        'research',
        'organization',
        'interest',
        'group_activity',
        'speaking',
        'frequencia_of',
        'listening',
        'readind_inter',
        'writing_process',
        'frequencia_pct',
        # 'media_final',

    ) # grid de visualizações
    # list_filter = ()
    search_fields = (
        'v_created_at',
        'v_week_at',
        'aluno',
    )
    @admin.display(description='Turma')
    def v_created_at(self, obj):
        return f'{obj.turma.created_at.year}-{obj.turma.created_at.month}'

    @admin.display(description='Horário')
    def v_week_at(self, obj):
        return f'{obj.turma.horario}'



    # filter_horizontal = ('aluno',)
    pass

