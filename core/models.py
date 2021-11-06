from django.db import models

#Import do campo usuario(No caso operador)
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, DO_NOTHING


class Tipo(models.Model):
    nome = models.CharField('Tipo' ,max_length=50)

    def __str__(self):
        return self.nome

class Controle(models.Model):
    placa = models.CharField('Placa', max_length=12)
    modelo = models.CharField('Modelo', max_length=30)
    tipo = models.CharField('Tipo', max_length=20)
    descricao = models.CharField('Descrição', max_length=200, blank=True)
    entrada = models.DateTimeField('Entrada', auto_now_add=True)

    operador = models.ForeignKey(User, on_delete=CASCADE)

    tipo = models.ForeignKey(Tipo, on_delete=DO_NOTHING)

    def __str__(self):
        return (self.placa)