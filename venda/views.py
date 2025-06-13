from django.shortcuts import render, redirect
from .models import Venda
from .forms import VendaForm

def venda_list(request):
    vendas = Venda.objects.all()
    return render(request, 'venda/list.html', {'vendas': vendas})

def venda_create(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venda_list')
    else:
        form = VendaForm()
    return render(request, 'venda/cadastro.html', {'form': form})