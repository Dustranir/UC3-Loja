from django.shortcuts import render, redirect
from .models import Venda
from .forms import VendaForm

def venda_create(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venda_list')
    else:
        form = VendaForm()
    return render(request, 'venda/venda_form.html', {'form': form})

def venda_list(request):
    vendas = Venda.objects.all().order_by('-data_venda')
    return render(request, 'venda/venda_list.html', {'vendas': vendas})

def index(request):
    return render(request, 'venda/index.html')
