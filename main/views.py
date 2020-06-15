from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from medicamento.models import Medicamento

# Create your views here.


def loginusuario(request):
    if request.method == 'GET':
        return render(request, 'main/login.html', {'formulario': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/login.html', {'formulario': AuthenticationForm(), 'erro': 'Usuário ou senha incorreta'})
        else:
            login(request, user)
            return redirect('home')


def home(request):
    if request.user.is_authenticated:
        medicamentos = Medicamento.objects.all()

        return render(request, 'main/home.html', {'medicamentos':medicamentos})
    else:
        return redirect('loginusuario')

@login_required
def logoutusuario(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
