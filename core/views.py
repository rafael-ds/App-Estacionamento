from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def entrada(request):
    return render(request, 'entrada.html')


def saida(request):
    return render(request, 'saida.html')

