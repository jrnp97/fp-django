""" Modulo para definicao de rotas do app"""
from django.urls import path
from .views import index, yury, carlos, carlos_two, conversor, PrimeiraCBView, SegundoConversor

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
]
