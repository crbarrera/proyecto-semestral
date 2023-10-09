from django.db import models

# Create your models here.
class Peliculas(models.Model):
    foto = models.ImageField(upload_to='images/')
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.nombre
