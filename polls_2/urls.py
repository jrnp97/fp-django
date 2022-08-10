""" Modulo para definicao de rotas do app"""
from django.urls import path
from .views import index, yury, carlos, carlos_two, conversor, PrimeiraCBView, SegundoConversor, IndexView, \
   TemplateView, ConversorSuperPower, lista_categorias, create_categoria, detail_categoria

# URLS Config do app
# Define a relacao entre um path e uma view
urlpatterns = [
   path('', index, name='index_polls_2'),

   # 2. Definir a url
   path('yury/', yury, name='yury_view'),

   # 2. Definir a url
   path('carlos/', carlos, name='carlos_view'),

   path('casa/carlos/', carlos_two, name='carlos_two'),

   # 2. Cadastro a url
   path('conversor/', conversor, name='conversor'),

   #2. Cadastro a url
   path('conversor_cbv/', PrimeiraCBView.as_view(), name='conversor_cbv'),

   #2. Cadastro a url
   path('conversor_new/', SegundoConversor.as_view(), name='conversor_new'),

   # 2. Cadastro url
   path('index_new/', IndexView.as_view(), name='index_new'),
   
   # 3. Renderizando um template directamente.
   path('index_refactor/', TemplateView.as_view(template_name='index.html'), name='index_refactor'),
   
   # 2. url
   path('power_conversor/', ConversorSuperPower.as_view(), name='power_conversor'),

   # 2.
   path('categorias/', lista_categorias, name='lista_categorias'),

   path('categorias/new/', create_categoria, name='create_categoria'),

   # 2. URL com parametros
   path('categorias/<int:id>/', detail_categoria, name='detail_categoria'),
]
