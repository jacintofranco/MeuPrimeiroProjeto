from django.http import HttpResponse
from django.shortcuts import render

from oladjango.models import Categorias


# Create your views here.



def olamundo(request):
    return HttpResponse('Ola Mundo')


# Pagina de teste de render
def paginaInicial(request):
    listaDeCategorias = Categorias.objects.all()
    context = {"listaDeCategorias":  listaDeCategorias}

    return render(request, "base.html", context)