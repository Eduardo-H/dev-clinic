from django.forms import ModelForm
from .models import Medicamento

class FormMedicamento(ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nome', 'marca', 'quantidade']
