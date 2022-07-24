from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . import models


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 4


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug' 


class AdicionarAoCarrinho(ListView):
    model = models.Produto
    template_name = 'produto/adicionaraocarrinho.html'
    context_object_name = 'produto'


class RemoverDoCarrinho(ListView):
    model = models.Produto


class Carrinho(ListView):
    model = models.Produto


class Finalizar(ListView):
    model = models.Produto
