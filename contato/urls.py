from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='contato_index'),
    path('', views.contato_create, name='contato_create'),
]