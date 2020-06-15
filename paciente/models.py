from django.db import models

# Create your models here.
class Paciente(models.Model):
    SEXO_CHOICES = (
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino')
    )


    nome = models.CharField(max_length=200)
    idade = models.BigIntegerField()
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=9, choices=SEXO_CHOICES)
    datadecadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
