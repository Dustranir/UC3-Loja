from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='clientes_index'),
    path('', views.cliente_list, name='cliente_list'),
    path('cadastro/', views.cliente_create, name='cliente_create'),
]