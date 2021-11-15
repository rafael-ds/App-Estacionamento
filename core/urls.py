from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('entrada/', views.entrada, name='entrada'),
    path('saida/', views.saida, name='saida'),
    path('saida_user/', views.saida_user, name='saida_user'),

    # path de remoção de veiculo
    path('del_saida/<int:id>', views.del_saida, name='del_saida'),

]