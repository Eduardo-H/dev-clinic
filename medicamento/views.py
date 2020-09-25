from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento
from .forms import FormMedicamento
from django.contrib.auth.decorators import login_required

@login_required
def menumedicamento(request):
    if request.method == 'GET':
        pesquisa = request.GET.get('nome')

        if not pesquisa:
            medicamentos = Medicamento.objects.all()
            return render(request, 'medicamento/menumedicamento.html', {'medicamentos':medicamentos})
        else:
            medicamentos = Medicamento.objects.filter(nome__contains=pesquisa)
            return render(request, 'medicamento/pesquisarmedicamento.html', {'medicamentos':medicamentos})

@login_required
def criarmedicamento(request):
    if request.method == 'GET':
        return render(request, 'medicamento/criarmedicamento.html', {'formulario':FormMedicamento()})
    else:
        repetido = Medicamento.objects.filter(nome=request.POST['nome'])

        if not repetido:
            try:
                medicamento = FormMedicamento(request.POST)
                medicamento.save()
                return redirect('../')
            except ValueError:
                return render(request, 'medicamento/criarmedicamento.html',
                {'formulario':FormMedicamento(), 'erro':'Não foi possível adicionar o medicamento'}
                )
        else:
            return render(request, 'medicamento/criarmedicamento.html', {'formulario':FormMedicamento(), 'erro':'Medicamento já existente'})

@login_required
def deletarmedicamento(request, pk_medicamento):
    medicamento = get_object_or_404(Medicamento, pk=pk_medicamento)

    if request.method == 'POST':
        medicamento.delete()
        return redirect('../../')

@login_required
def editarmedicamento(request, pk_medicamento):
    medicamento = get_object_or_404(Medicamento, pk=pk_medicamento)
    if request.method == 'GET':
        formulario = FormMedicamento(instance=medicamento)
        return render(request, 'medicamento/editarmedicamento.html', {'medicamento':medicamento, 'formulario':formulario})
    else:
        try:
            formulario = FormMedicamento(request.POST, instance=medicamento)
            formulario.save()
            return redirect('../../')
        except ValueError:
            return render(request, 'medicamento/editarmedicamento.html', {'medicamento':medicamento, 'formulario':formulario, 'erro':'Não foi possível atualizar o medicamento'})
