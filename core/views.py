from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def entrada(request):
    return render(request, 'entrada.html')

