from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Equipamento
from .form import EquipamentoForm

@login_required
def lista_equipamentos(request):
    lista = Equipamento.objects.all()
    return render(request, 'lista.html', {'lista': lista})

@login_required
def novo_equipamento(request):
    form = EquipamentoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'cadastro.html', {'form': form})

@login_required
def atualizar_equipamento(request, id):
    equip = get_object_or_404(Equipamento, pk=id)
    form = EquipamentoForm(request.POST or None, request.FILES or None, instance= equip)

    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'atualiza.html', {'form': form, 'equip':equip})

@login_required
def deleta_equipamento(request, id):
    equip = get_object_or_404(Equipamento, pk=id)
    form = EquipamentoForm(request.POST or None, request.FILES or None, instance= equip)

    if request.method == 'POST':
        equip.delete()
        return redirect('lista')
    return render(request, 'deleta.html', {'equip': equip})
