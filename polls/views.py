from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# VIEW
def primeira_view(request):
    return HttpResponse('Hola Mundo')

