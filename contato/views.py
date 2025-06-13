from django.shortcuts import render, redirect
from .models import Contato
from .forms import ContatoForm

def contato_create(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContatoForm()
    return render(request, 'contato/cadastro.html', {'form': form})