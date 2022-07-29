from django.urls import path
from .views import primeira_view

# Temos que respeitar esse nome `urlpatterns`
urlpatterns = [
    path('', primeira_view, name='first_view')
    # Signature: path(<path: str>, <view: Funcao>, <name: str>)
]
