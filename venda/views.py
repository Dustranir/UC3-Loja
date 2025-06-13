from django.shortcuts import render, redirect
from .models import Venda
from clientes.models import Cliente
from produtos.models import Produto
from django import forms

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'produto', 'quantidade']

def venda_list(request):
    vendas = Venda.objects.all().order_by('-data_venda')
    return render(request, 'venda/list.html', {'vendas': vendas})

def venda_create(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venda_list')
    else:
        form = VendaForm()
    return render(request, 'venda/form.html', {'form': form})