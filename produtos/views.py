from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/list.html', {'produtos': produtos})

def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/cadastro.html', {'form': form})