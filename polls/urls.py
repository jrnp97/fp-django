from django.urls import path
from .views import primeira_view

urlpatterns = [
    path('', primeira_view, name='first_view')
]
