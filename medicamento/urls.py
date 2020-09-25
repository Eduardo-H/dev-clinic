from django.urls import path
from . import views

app_name = 'medicamento'

urlpatterns = [
    path('', views.menumedicamento, name='menumedicamento'),
    path('criar/', views.criarmedicamento, name='criarmedicamento'),
    path('<int:pk_medicamento>/deletar/', views.deletarmedicamento, name='deletarmedicamento'),
    path('<int:pk_medicamento>/editar/', views.editarmedicamento, name='editarmedicamento'),
]
