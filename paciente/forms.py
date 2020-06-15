from django.forms import ModelForm
from .models import Paciente

class FormPaciente(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'idade', 'cpf', 'sexo']
