"""dev_clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('login/', views.loginusuario, name="loginusuario"),
    path('logout/', views.logoutusuario, name='logoutusuario'),

    # Inclusões de urls de outros apps
    path('paciente/', include('paciente.urls')),
    path('colaboracao/', include('colaboracao.urls')),
    path('medicamento/', include('medicamento.urls')),
]
