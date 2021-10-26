from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('entrada/', views.entrada, name='entrada'),
    path('saida/', views.saida, name='saida'),
    path('saida_user/', views.saida_user, name='saida_user'),
]