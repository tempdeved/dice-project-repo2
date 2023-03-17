from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'nome_completo',
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
        'mes_nascimento',
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


# @admin.register(models.Horario)
# class HorarioAdmin(admin.ModelAdmin):
#     # fields = () #campos para cadastrar
#     list_display = (
#         'dia_semana',
#         'hr_turma',
#     ) # grid de visualizações
#     # list_filter = ()
#     # search_fields = ()
#     # filter_horizontal = ('aluno',)
#     @admin.display(description='Hora')
#     def v_hora(self, obj):
#         return f'{obj.hora_inicio}:{obj.min_inicio}-' \
#            f'{obj.hora_fim}:{obj.min_fim}'
#     pass

@admin.register(models.Turma)
class TurmaAdmin(admin.ModelAdmin):
    # fields = () #campos para cadastrar
    list_display = (
        'v_created_at',
        'dia_semana',
        'hr_turma',
        'status',
    ) # grid de visualizações
    list_filter = (
        'created_at',
        'status',
    )
    # search_fields = ()
    filter_horizontal = ('aluno',)

    @admin.display(description='Ano')
    def v_created_at(self, obj):
        return f'{obj.created_at.year}'

    @admin.display(description='Dia Semana')
    def dia_semana(self, obj):
        return f'{obj.dia_semana}'

    @admin.display(description='Hora')
    def hr_turma(self, obj):
        try:
            return f'{self.hora_inicio}:{self.min_inicio} - ' \
                   f'{self.hora_fim}:{self.min_fim}'.upper()
        except:
            return f'Não Cadastrado'

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
        'coment2',
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

