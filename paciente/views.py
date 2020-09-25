from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from django.contrib.auth.decorators import login_required
from .forms import FormPaciente
from django.urls import reverse


@login_required
def menupaciente(request):
    if request.method == 'GET':
        pesquisa = request.GET.get('nome')

        if not pesquisa:
            pacientes = Paciente.objects.order_by('-datadecadastro')[:4]
            return render(request, 'paciente/menupaciente.html', {'pacientes':pacientes})
        else:
            pacientes = Paciente.objects.filter(nome__contains=pesquisa)
            return render(request, 'paciente/pesquisapaciente.html', {'pacientes':pacientes})

@login_required
def criarpaciente(request):
    if request.method == 'GET':
        paciente = Paciente()
        return render(request, 'paciente/criarpaciente.html', {'formulario':FormPaciente(), 'paciente':paciente})
    else:
        cpf = request.POST['cpf']
        if len(cpf) == 11:
            repetido = Paciente.objects.filter(cpf=request.POST['cpf'])
            if not repetido:
                try:
                    paciente = FormPaciente(request.POST)
                    paciente.save()
                    return redirect('../')
                except ValueError:
                    return render(request, 'paciente/criarpaciente.html', {'formulario':FormPaciente(), 'erro':'Não foi possível cadastrar o(a) paciente'})
            else:
                return render(request, 'paciente/criarpaciente.html', {'formulario':FormPaciente(), 'erro':'CPF já cadastrado'})
        else:
            return render(request, 'paciente/criarpaciente.html', {'formulario':FormPaciente(), 'errocpf':'O CPF deve ter 11 caracteres'})

@login_required
def verpaciente(request, pk_paciente):
    paciente = get_object_or_404(Paciente, pk=pk_paciente)
    return render(request, 'paciente/verpaciente.html', {'paciente':paciente})


@login_required
def editarpaciente(request, pk_paciente):
    if request.method == 'GET':
        paciente = get_object_or_404(Paciente, pk=pk_paciente)
        formulario = FormPaciente(instance=paciente)
        return render(request, 'paciente/editarpaciente.html', {'formulario':formulario, 'paciente':paciente})
    else:
        try:
            formulario = FormPaciente(request.POST, instance=paciente)
            formulario.save()
            return redirect('paciente:menupaciente')
        except ValueError:
            return render(request, 'paciente/editarpaciente.html', {'formulario':formulario, 'erro':'Não foi possível editar o paciente'})

@login_required
def deletarpaciente(request, pk_paciente):
    paciente = get_object_or_404(Paciente, pk=pk_paciente)

    if request.method == 'POST':
        paciente.delete()
        return redirect('paciente:menupaciente')
