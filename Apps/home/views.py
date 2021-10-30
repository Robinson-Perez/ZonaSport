from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Cliente, Reservas, Usuario
from .forms import ClienteForm, RegistroForm,  ReservaForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
class Home2view(TemplateView):
    template_name='index-2.html'

class listarclientes(ListView):
    template_name='clientes_list.html'
    model = Cliente

class AgregarCliente(CreateView):
    template_name = 'crear_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('home2')

class NuevaR(CreateView):
    template_name = 'calendario.html'
    form_class = ReservaForm
    success_url = reverse_lazy('home2')

class Reserva(ListView):
    template_name = 'reservado.html'
    model=Reservas

#class Loginview(TemplateView):
    #template_name='login.html'

class RegistroView(CreateView):
    model=Usuario
    form_class=RegistroForm
    success_url = reverse_lazy('home2')
    
class Homeview(TemplateView):
    template_name='index.html'

class Noticiasview(TemplateView):
    template_name='noticias.html'
    
class Deportivoview(TemplateView):
    template_name='deportivo.html'

class Tiendaview(TemplateView):
    template_name='tienda.html'

class Reservasview(TemplateView):
    template_name='contact.html'

class LoginView(LoginView):
    template_name='login.html'

def logout_request(request):
    logout(request)
    messages.info(request, "Fin de la sesion")
    return redirect("home")

def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario =form.cleaned_data.get('username')
            contraseña=form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                login(request, user)
                messages.info(request, "Bienvenido {usuario}")
                return redirect("home2")

            else:
                messages.error(request, "Usuario o contraseña incorrecta")
        else:
                messages.error(request, "Usuario o contraseña incorrecta")

    form= AuthenticationForm()
    return render(request, "login.html", {"form":form})
