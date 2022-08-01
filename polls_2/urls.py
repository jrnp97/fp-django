""" Modulo para definicao de rotas do app"""
from django.urls import path
from .views import index, yury, carlos, carlos_two

# URLS Config do app
# Define a relacao entre um path e uma view
urlpatterns = [
   path('', index, name='index_polls_2'),

   # 2. Definir a url
   path('yury/', yury, name='yury_view'),

   # 2. Definir a url
   path('carlos/', carlos, name='carlos_view'),

   path('casa/carlos/', carlos_two, name='carlos_two')
]
