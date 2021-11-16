from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # views de login
    path('home/', views.home, name='home'),# views de Home
    path('entrada/', views.entrada, name='entrada'), # views de Cadastro de entrada
    path('saida/', views.saida, name='saida'),# views de lieração de veiculos
    path('saida_user/', views.saida_user, name='saida_user'), # views de logigout de usuario
    path('buscar/', views.buscar, name='buscar'),# views de busca po veiculo

    # path de remoção de veiculo
    path('del_saida/<int:id>', views.del_saida, name='del_saida'),

]