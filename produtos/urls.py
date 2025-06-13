from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='produtos_index'),
    path('', views.produto_list, name='produto_list'),
    path('cadastro/', views.produto_create, name='produto_create'),
]