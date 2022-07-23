from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View


class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('listar')


class DetalheProduto(ListView):
    pass


class AdicionarAoCarrinho(ListView):
    pass


class RemoverDoCarrinho(ListView):
    pass


class Carrinho(ListView):
    pass


class Finalizar(ListView):
    pass




