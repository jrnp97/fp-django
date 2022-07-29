from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# View: Funcoes
# signature: (request: Object) -> HttpResponse
def index(request):
    return HttpResponse('<h1>Hola</h1>')


# 1. View: SEMPRE PRECISA RETORNAR UM HttpResponse
def yury(request):
    return HttpResponse('<h1>Yury solicitou</h1>')


# 1. View
def carlos(request):
    name = "jaime"
    cores = [
        "mimosa",
        "verde",
        "vermelho",
    ]
    return render(request=request, template_name='index.html', context={'name': name, 'cores': cores})
