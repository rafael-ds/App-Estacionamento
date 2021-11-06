from django.shortcuts import render, redirect
from django.contrib import messages, auth
from datetime import datetime as dt

#Importe que tem como objetivo a necessidade de estar logado
#para ter acesso a determinada pagina
from django.contrib.auth.decorators import login_required

# Import para realização de login e logout
from django.contrib.auth import logout

from .models import Controle, Tipo

# Função index
def index(request):
    if request.method != 'POST':
        messages.info(request, 'Entre com o usuario e senha para logar.')
        return render(request, 'index.html')

    usuario = request.POST.get('operador')
    senha = request.POST.get('senha')

    operador = auth.authenticate(request, username=usuario, password=senha)

    if not operador:
        messages.error(request, 'Nome de usuário ou senha estão incorretos')
        return render(request, 'index.html')

    else:
        auth.login(request, operador)
        return redirect('home')


    return render(request, 'index.html')
# Fim da index

# Logout
# ATENÇÃO: NOME DA FUNÇÃO NÃO PODE SER RESERVADA
@login_required(redirect_field_name='index')
def saida_user(request):
    logout(request)
    return redirect('index')
# Fim Logout 


# Home
@login_required(redirect_field_name='index')
def home(request):

    veiculos = Controle.objects.all()

    contexto = {
        'veiculo': veiculos
    }

    return render(request, 'home.html', contexto)
# Fim da Home


# Entrada 
@login_required(redirect_field_name='index')
def entrada(request):

    if request.method != 'POST':
        return render(request, 'entrada.html')

    elif request.method == 'POST':
        placa = request.POST.get('placa')
        modelo = request.POST.get('modelo')
        tipo = Tipo(request.POST.get('tipo'))
        desc = request.POST.get('desc')

        operador = request.user

        if not placa or not modelo or not tipo:
            messages.warning(request, 'Os campos Placa, Modelo e Tipo são obrigatorios')
            return render(request, 'entrada.html')

        veiculo = Controle.objects.create(placa=placa, modelo=modelo, tipo=tipo, descricao=desc, operador=operador,)


        if veiculo:
            return redirect('home')

    return render(request, 'entrada.html')
# Fim da entrada


# Saída
@login_required(redirect_field_name='index')
def saida(request):

    # variavel de retorna a placa digitada
    get_placa = request.GET.get('buscarPlaca')
    
    veiculo = Controle.objects.order_by('id').filter(
        # variavel placa --> Vem do Banco
        #get_placa --> Vem da busca saida.html
        placa=get_placa,
    )

    # Inserindo a hora atual do sistema
    h_atual = dt.now().strftime('%H:%M')
    
    contexto = {
        'veiculo': veiculo,
        'horas': h_atual,
    }


    return render(request, 'saida.html', contexto)
# Fim da saída
