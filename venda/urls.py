from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='vendas_index'),
    path('', views.venda_list, name='venda_list'),
    path('cadastro/', views.venda_create, name='venda_create'),
    
]