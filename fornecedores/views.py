from django.shortcuts import render, redirect, get_object_or_404
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

def index(request):
    return render(request, 'fornecedores/index.html')

def fabricante_delete(request, pk):
    fornecedor = get_object_or_404(Fabricante, pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('produto_list')  
    return render(request, 'fornecedores/deletar_fornecedor.html', {'fornecedor': fornecedor})