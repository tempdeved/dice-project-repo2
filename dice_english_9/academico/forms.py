from django.forms import ModelForm
from . import models


class AlunoForm(ModelForm):
    class Meta:
        model = models.Aluno
        fields = '__all__'