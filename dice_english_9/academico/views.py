from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    request = 'ola, mundo'
    response = HttpResponse(request)
    return response

def aluno(request):
    request = 'ola, ALuno'
    response = HttpResponse(request)
    return response

def aluno_id(request, id):
    request = f'ola, ID: {id}'
    response = HttpResponse(request)
    return response
