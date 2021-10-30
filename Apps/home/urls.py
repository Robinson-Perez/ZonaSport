"""Test URL home Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from .import views
from .views import AgregarCliente, Deportivoview, Homeview, Noticiasview, NuevaR, Reserva, RegistroView, Reservasview, Tiendaview,  listarclientes,  Home2view
urlpatterns = [
    
    path('index-2/',  Home2view.as_view(), name='home2'),
    path('calendario/',  NuevaR.as_view(), name='calendario'),
    path('listarclientes/',  listarclientes.as_view(), name='clientes_list'),
    path('crearcliente/', AgregarCliente.as_view(),  name = 'new_cliente'),
    path('reservado/',  Reserva.as_view(), name='reservado'),
    path('registro/',  RegistroView.as_view(), name='registro'),
    path('index/',  Homeview.as_view(), name='home'),
    path('noticias/',  Noticiasview.as_view(), name='noticias'),
    path('deportivo/',  Deportivoview.as_view(), name='deportivo'),
    path('tienda/',  Tiendaview.as_view(), name='tienda'),
    path('contact/',  Reservasview.as_view(), name='contact'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name= 'login'),
]
