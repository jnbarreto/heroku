from django.forms import ModelForm
from .models import Equipamento

class EquipamentoForm(ModelForm):
    class Meta:
        model = Equipamento
        fields = ['tipo','marca','modelo','num_controle','img_equip']