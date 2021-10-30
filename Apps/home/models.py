from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Cliente(models.Model):
  doc = (
     ('PASPORT','Pasaporte'),
     ('DPI','DPI'),
)
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  direccion = models.CharField(max_length=200)
  documento = models.CharField(
     max_length=20,
     choices=doc,
     default=''
 )
  no_doc = models.CharField(max_length=200)
  imagen=models.CharField(max_length=500, default="")
  nacimiento = models.DateField()
  correo = models.CharField(max_length=50)
  telefono= models.CharField(max_length=10)
  creacion = models.DateField(auto_now_add=True)
  actualizacion = models.DateField(auto_now_add=True)
 
  def __str__(self) -> str:
     return '%s  %s'%(self.nombre,self.apellido)


class Reservas(models.Model):
   pago=(
      ('Total','Cancelado'),
      ('Anticipo', 'Anticipo'),
   )
   horario = (
     ('08:00-09:00','8 AM'),
     ('09:00-10:00','9 AM'),
     ('10:00-11:00','10 AM'),
     ('11:00-12:00','11 AM'),
     ('12:00-13:00','12 PM'),
     ('13:00-14:00','1 PM'),
     ('14:00-15:00','2 PM'),
     ('15:00-16:00','3 PM'),
      ('16:00-17:00','4 PM'),
      ('17:00-18:00','5 PM'),
      ('18:00-19:00','6 PM'),
      ('19:00-20:00','7 PM'),
      ('20:00-21:00','8 PM'),
)
   nombre = models.ForeignKey(
   'Cliente',
   on_delete=models.CASCADE,
   default=1
  )
   fecha = models.DateField()
   hora = models.CharField(
     max_length=20,
     choices=horario,
     default=''
 )
   telefono=models.CharField(max_length=12)
   correo = models.CharField(max_length=50)
   pago =models.CharField(
      max_length=20,
      choices=pago,
      default=''
   )
   monto=models.CharField(max_length=12)
   creacion = models.DateField(auto_now_add=True)
   actualizacion = models.DateField(auto_now_add=True)
 
   def __str__(self) -> str:
     return '%s  %s'%(self.nombre,self.hora)

class Usuario(models.Model):
   perfil= models.OneToOneField(User, on_delete=models.CASCADE)

   def __str__(self):
       return self.perfil.username 

@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
   if created:
      Usuario.objects.create(perfil=instance)

@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
   instance.usuario.save()