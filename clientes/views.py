from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/list.html', {'clientes': clientes})

def cliente_delete(request, cpf):
    cliente = get_object_or_404(Cliente, cpf=cpf)
    cliente.delete()
    messages.success(request, f"Cliente {cliente.nome} excluído com sucesso.")
    return redirect('cliente_list')

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso.")
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastro.html', {'form': form})

def index(request):
    return render(request, 'clientes/index.html')