from django.urls import path
from . import views

app_name = 'colaboracao'

urlpatterns = [
    path('', views.menucolaboracao, name='menucolaboracao'),
    path('criar/', views.criarcolaboracao, name='criarcolaboracao'),
    path('<int:pk_colaboracao>/deletar/', views.deletarcolaboracao, name='deletarcolaboracao'),
    path('<int:pk_colaboracao>/detalhes/', views.vercolaboracao, name='vercolaboracao'),
]
