from django.contrib import admin
from .models import Cliente, Reservas, Usuario

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Reservas)
admin.site.register(Usuario)
