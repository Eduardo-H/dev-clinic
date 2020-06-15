from django.forms import ModelForm
from .models import Colaboracao
from paciente.models import Paciente

class FormColaboracao(ModelForm):
    class Meta:
        model = Colaboracao
        fields = ['paciente', 'medicamento']

class FormProcuraPaciente(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome']
