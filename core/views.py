from django.core import paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages, auth
from datetime import datetime as dt

from django.core.paginator import Paginator

#Importe que tem como objetivo a necessidade de estar logado
#para ter acesso a determinada pagina
from django.contrib.auth.decorators import login_required

# Import para realização de login e logout
from django.contrib.auth import logout

# Models
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

    # Inicio da paginação
    paginator = Paginator(veiculos, 5) # objeto de paginação 
    page = request.GET.get('p')
    veiculos = paginator.get_page(page)
    # Fim da paginação
    
    contexto = {
        'veiculo': veiculos,
    }

    return render(request, 'home.html', contexto)
# Fim da Home

@login_required(redirect_field_name='index')
def buscar(request):

    get_placa = request.GET.get('buscarPlaca')

    buscar = Controle.objects.order_by('id').filter(
        placa=get_placa
    )

    contexto = {
        'buscar': buscar
    }
    
    return render(request, 'buscar.html', contexto)


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
    
    if  not veiculo:
        messages.info(request, 'Placa não encontrada.')
        return render(request, 'saida.html')

    # Lógica de pagamento
    get_saida = Controle.objects.get(placa=get_placa)
    
    # Capturando o horario de entrada
    h_entrada = get_saida.entrada
    h_atual = dt.now()

    # Calculando a hora atual menos a hora de entrada para
    # definir o valor do rotativo
    total_horas = h_atual.hour - h_entrada.hour

    valor = (total_horas * 4)

    # Inserindo a hora atual no templates
    mostra_horas = dt.now().strftime('%H:%M')
    
    contexto = {
        'veiculo': veiculo,
        'horas': mostra_horas,
        'valor': valor
    }

    return render(request, 'saida.html', contexto)
# Fim da saída

# Função que remove o item de BD
@login_required(redirect_field_name='index')
def del_saida(request, id):
    veiculo = get_object_or_404(Controle, pk=id)
    
    if veiculo:
        messages.success(request, 'Veiculo Liberado.')
        veiculo.delete()
        return redirect('home')

    return redirect('saida')
