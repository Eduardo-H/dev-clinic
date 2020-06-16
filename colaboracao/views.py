from django.shortcuts import render, redirect, get_object_or_404
from .models import Colaboracao
from django.contrib.auth.decorators import login_required
from .forms import FormColaboracao, FormProcuraPaciente
from paciente.models import Paciente
from medicamento.models import Medicamento
from django.db.models import Q

@login_required
def menucolaboracao(request):
    colaboracoes = Colaboracao.objects.order_by('-data')
    return render(request, 'colaboracao/menucolaboracao.html', {'colaboracoes':colaboracoes})


@login_required
def criarcolaboracao(request):
    if request.method == 'GET':
        consulta = request.GET.get('nome')

        if consulta is not None:
            global paciente
            paciente = Paciente.objects.filter(nome__contains=consulta)
            global medicamentos
            medicamentos = Medicamento.objects.all()
            return render(request, 'colaboracao/criarcolaboracaofinal.html', {'formulario':FormColaboracao(), 'pacientes':paciente, 'medicamentos':medicamentos})
        else:
            return render(request, 'colaboracao/criarcolaboracao.html', {'procurapaciente':FormProcuraPaciente()})
    else:
        formulario = FormColaboracao(request.POST)
        print(formulario)
        try:
            formulario = FormColaboracao(request.POST)
            formulario.save()
            return redirect('../')
        except ValueError:
            return render(request, 'colaboracao/criarcolaboracaofinal.html',
            {'formulario':FormColaboracao(), 'pacientes':paciente,
            'medicamentos':medicamentos, 'erro':'Não foi possível adicionar a colaboração'}
            )

@login_required
def deletarcolaboracao(request, pk_colaboracao):
    colaboracao = get_object_or_404(Colaboracao, pk=pk_colaboracao)
    if request.method == 'POST':
        colaboracao.delete()
        return redirect('menucolaboracao')

@login_required
def vercolaboracao(request, pk_colaboracao):
    colaboracao = get_object_or_404(Colaboracao, pk=pk_colaboracao)
    return render(request, 'colaboracao/vercolaboracao.html', {'colaboracao':colaboracao})

##########
# Função #
##########

def procurarpacientepornome(nomepaciente):
    nomes = Paciente.objects.filter(nome__contains=nomepaciente)
    return nomes
