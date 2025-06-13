from django.shortcuts import render, redirect
from .models import Fabricante
from .forms import FabricanteForm

def fornecedor_list(request):
    fabricantes = Fabricante.objects.all()
    return render(request, 'fornecedores/list.html', {'fabricantes': fabricantes})

def fornecedor_create(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_list')
    else:
        form = FabricanteForm()
    return render(request, 'fornecedores/cadastro.html', {'form': form})