from django.db import models

# Create your models here.
class Medicamento(models.Model):
    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=60, blank=True)
    quantidade = models.BigIntegerField()

    def __str__(self):
        return self.nome
