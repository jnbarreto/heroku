from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Equipamento


class ListEquipamentos(ListView):
    model = Equipamento


class DetailEquipamentos(DetailView):
    model = Equipamento


class NewEquipamento(CreateView):
    model = Equipamento
    fields = ['tipo', 'marca', 'modelo', 'num_controle', 'img_equip']

    def get_success_url(self):
        return reverse_lazy('list')


class UpdateEquipamento(UpdateView):
    model = Equipamento
    fields = ['tipo', 'marca', 'modelo', 'num_controle', 'img_equip']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('list')


class DeleteEquipamento(DeleteView):
    model = Equipamento

    def get_success_url(self):
        return reverse_lazy('list')
