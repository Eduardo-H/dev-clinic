from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [
    path('', views.menupaciente, name='menupaciente'),
    path('criar/', views.criarpaciente, name='criarpaciente'),
    path('<int:pk_paciente>/detalhes/', views.verpaciente, name='verpaciente'),
    path('<int:pk_paciente>/editar/', views.editarpaciente, name='editarpaciente'),
    path('<int:pk_paciente>/deletar', views.deletarpaciente, name='deletarpaciente'),

]
