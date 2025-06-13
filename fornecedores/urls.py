from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='fornecedores_index'),
    path('', views.fornecedor_list, name='fornecedor_list'),
    path('cadastro/', views.fornecedor_create, name='fornecedor_create'),
]