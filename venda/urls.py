from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='vendas_index'),
    path('cadastro/', views.venda_create, name='venda_create'),
    path('', views.venda_list, name='venda_list')
    
]