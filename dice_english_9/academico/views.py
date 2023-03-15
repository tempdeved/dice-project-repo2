from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms

# Create your views here.
# def home(request):
#     request = 'ola, mundo'
#     response = HttpResponse(request)
#     return response
def home(request):

    result = {
        'hello': 'ola mundo, home',
        'div_teste': 'teste-div',
    }

    response = render(
        request=request,
        template_name='index.html',
        context=result,
    )

    return response

def alunos(request):

    alunos = models.Aluno.objects.all()

    form = forms.AlunoForm()

    result = {
        'alunos': alunos,
        'form': form
    }

    response = render(
        request=request,
        template_name='alunos.html',
        context=result,
    )

    return response

def aluno_novo(request):
    form = forms.AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('aluno')


def turmas(request):


    turmas = models.Turma.objects.all()

    result = {
        'turmas': turmas
    }

    for i in turmas:
        print(f'kkkkk - {i}')

    response = render(
        request=request,
        template_name='turmas.html',
        context=result,
    )

    return response

def aluno(request):
    request = 'ola, ALuno'
    response = HttpResponse(request)
    return response

def aluno_id(request, id):
    request = f'ola, ID: {id}'
    response = HttpResponse(request)
    return response
