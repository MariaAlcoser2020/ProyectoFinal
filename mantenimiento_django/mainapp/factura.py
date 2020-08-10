from django.shortcuts import render, redirect
from .models import Factura


def listar(request):
    lista = Factura.objects.all().order_by('pk')
    data = {'menu': 'Facturas',
                'modulo': 'Factura',
                'listado': lista}
    return render(request, 'factura/listar.html', data)
