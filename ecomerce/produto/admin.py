from django.contrib import admin
from . models import Produto, Variacao
from . import models

class VariacaoInLine(admin.TabularInline):
    model = models.Variacao
    extra = 3

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','descricao_curta','preco_marketing','preco_marketing_promocional']
    inlines = [
        VariacaoInLine
    ]

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
