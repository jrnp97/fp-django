from django.http import HttpResponse
from django.shortcuts import render, redirect


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
from .forms import LoginForm
# 1 View.
# DIY: Don't Repeat Yourself
def carlos_two(request):
    name = "jaime"
    cores = [
        "mimosa",
        "verde",
        "vermelho",
    ]
    form = LoginForm()
    response = loader.render_to_string(
        template_name='index.html',
        context={'name': name, 'cores': cores, 'form': form},
        request=request,
    )
    return HttpResponse(response)


# 1. View
# 1. Importamos ele
from .forms import Conversor, CategoryForm
def conversor(request):
    # Preciso criar uma instancia do formulario
    # Como acessar as informacoes do formulario enviadas na request.
    if request.method == 'POST':
        form = Conversor(request.POST)
        if form.is_valid():
            print("OS DADOS SAO VALIDOS!!!")
    else:
        form = Conversor()
    print("[FUNCTION] ENTROU AQUI NA VIEW!!!")
    return render(
        request=request,
        template_name='polls_2/conversor.html',
        context={
            'form': form,
        }
    )

# 1. CBV [Class-Based Views] - Organizacao do codigo melhorando a legibilidade.
# 2. Caracteristica do POO a reusabilidade de codigo.
# 3. Caracteristica do POO Herencia
## 1. Define a View - Clase
from django.views import View

class PrimeiraCBView(View):
    template = 'polls_2/conversor.html'
    def __render(self, context, request):
        return render(request=request,
            template_name=self.template,
            context=context
        )
    def post(self, request):
        form = Conversor(request.POST)
        if form.is_valid():
            print("OS DADOS SAO VALIDOS!!!")
        return self.__render(request=request,
            context={'form': form}
        )
    def get(self, request):
        print("[CLASS] ENTROU AQUI NA VIEW!!!")
        form = Conversor()
        return self.__render(request=request,
            context={'form': form}
        )


class SegundoConversor(PrimeiraCBView):
    template = 'polls_2/conversor_2.html'


# DRY: Don't Repeat Yourself
# Generic Views: Sao views que tem comportamentos padrao.
# 1. Renderizar simplesmente um template.
from django.views.generic import TemplateView

# 1. View
class IndexView(TemplateView):
    template_name = 'index.html'


# 2. Renderizar um formulario
from django.views.generic import FormView


class ConversorSuperPower(FormView):
    form_class = Conversor
    template_name = 'polls_2/conversor.html'


from .models import Category

def lista_categorias(request):
    categorias = Category.objects.all()
    return render(
        request=request,
        template_name='polls_2/lista_categorias.html',
        context={
            'categorias': categorias,
        }
    )


def create_categoria(request):
    from .forms import CategoryForm
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            print("DADOS VALIDADOS!!!")
            return redirect('lista_categorias')
    else:
        form = CategoryForm()
    return render(
        request=request,
        template_name='polls_2/create_categoria.html',
        context={'form': form},
    )

def detail_categoria(request, id):
    categoria = Category.objects.get(category_id=id)
    return render(
        request=request,
        template_name='polls_2/detail_categoria.html',
        context={'categoria': categoria},
    )


def update_categoria(request, id):
    categoria = Category.objects.get(category_id=id)
    if request.method == 'GET':
        form = CategoryForm(instance=categoria)
    elif request.method == 'POST':
        form = CategoryForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            print("Actualizado!!!")
            return redirect('lista_categorias')

    return render(
        request,
        template_name='polls_2/create_categoria.html',
        context={'form': form, 'update': True, 'categoria': categoria},
    )

def delete_categoria(request, id):
    categoria = Category.objects.get(category_id=id)
    categoria.delete()
    return redirect('lista_categorias')
