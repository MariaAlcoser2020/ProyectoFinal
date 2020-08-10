from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm


def listar(request):
    lista = Cliente.objects.all().order_by('pk')
    data = {'menu': 'Mantenimiento Cliente',
                'modulo': 'Clientes',
                'listado': lista}
    return render(request, 'cliente/listar.html', data)


def registrar(request):
    data = {'menu': 'Mantenimiento Cliente',
                'modulo': 'Registrar Clientes',
                }

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_listado')
    else:
        form = ClienteForm()
        data['form'] = form
    return render(request, 'cliente/form.html', data)


def editar(request, id):
    data = {'menu': 'Mantenimiento Cliente',
                'modulo': 'Modificar Clientes',
                }
    cli_obj = Cliente.objects.get(id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cli_obj)
        if form.is_valid():
            form.save()
            return redirect('clientes_listado')
    else:
        form = ClienteForm(instance=cli_obj)
        data['formulario'] = form
    return render(request, 'cliente/form.html', data)


def eliminar(request, id):
    cli_obj = Cliente.objects.get(id=id)
    data = {'menu': 'Mantenimiento Cliente',
                'modulo': 'Eliminar Clientes',
                'registro': cli_obj
                }
    if request.method == 'POST':
        cli_obj.delete()
        return redirect('clientes_listado')
    return render(request, 'cliente/eliminar.html', data)
