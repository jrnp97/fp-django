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


# render é um shortcut
from django.template import loader
# 1 View.
# DIY: Don't Repeat Yourself
def carlos_two(request):
    name = "jaime"
    cores = [
        "mimosa",
        "verde",
        "vermelho",
    ]
    response = loader.render_to_string(
        template_name='index.html',
        context={'name': name, 'cores': cores},
        request=request,
    )
    return HttpResponse(response)

