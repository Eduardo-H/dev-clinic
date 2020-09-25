from django.db import models
from paciente.models import Paciente
from medicamento.models import Medicamento


class Colaboracao(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
