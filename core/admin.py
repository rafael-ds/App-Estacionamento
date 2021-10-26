from django.contrib import admin

from .models import Controle, Tipo

@admin.register(Controle)
class BdControleAdmim(admin.ModelAdmin):
    list_display = ('id', 'placa', 'modelo', 'tipo', 'descricao', 'operador')


@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)