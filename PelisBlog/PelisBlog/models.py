from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    idprod = models.IntegerField(primary_key=True, verbose_name='ID Prod')
    nomprod = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nombre')
    descprod = models.CharField(max_length=300, null=False, blank=False, verbose_name='Descripción')
    precio = models.IntegerField(null=False, blank=False, verbose_name='Precio')

    class Meta:
        db_table = 'Producto'
    
    def __str__(self):
        return f'{self.idprod} - {self.nomprod}'
    
