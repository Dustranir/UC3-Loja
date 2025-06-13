from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastro.html', {'form': form})