from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Peliculas(models.Model):
    foto = models.ImageField(upload_to='images/')
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.nombre

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=40, default="Sin Rut", null=True, blank=True)
    direccion = models.CharField(max_length=100, null=False, blank=False, verbose_name='direccion')
    comuna = models.CharField(max_length=100, null=False, blank=False, verbose_name='comuna')
    telefono = models.IntegerField()
    region = models.CharField(max_length=100, null=False, blank=False, verbose_name='region')
    
    def __str__(self) -> str:
        return f"{self.user.username}"

class Factura(models.Model):
    codigo_factura = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=90, null=True)
    monto_producto = models.IntegerField(default=1, blank=True, null=True)
    precio_producto = models.IntegerField()
    fecha_factura = models.DateTimeField(auto_now=True)
    estado_factura = models.CharField(max_length=40 ,default="Pendiente", null=True, blank=True)
    