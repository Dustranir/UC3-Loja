from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='login_index'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]