"""
URL configuration for estancol project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from inicio import views as Inicio
from nosotros import views as Nosotros
from productos import views as Productos
from servicios import views as Servicios
from contactenos import views as Contactenos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio.cargarInicio , name='inicio'),
    path('nosotros/', Nosotros.cargarInicio , name='nosotros'),
    path('productos/', Productos.cargarInicio , name='productos'),
    path('servicios/', Servicios.cargarInicio , name='servicios'),
    path('contactenos/', Contactenos.cargarInicio , name='contactenos'),
    path('enviar_correo/', Inicio.enviar_correo, name='enviar_correo'),
]
