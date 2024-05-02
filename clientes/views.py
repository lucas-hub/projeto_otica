from django.shortcuts import render, redirect
from .forms import VendaForm

def cadastrar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes/cadastrar_venda.html')  # Certifique-se que este caminho está correto
    else:
        form = VendaForm()
    return render(request, 'clientes/cadastrar_venda.html', {'form': form})
