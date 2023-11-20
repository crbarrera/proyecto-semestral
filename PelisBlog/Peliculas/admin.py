from django.contrib import admin
from .models import Peliculas, PerfilUsuario, Factura
# Register your models here.
admin.site.register(Peliculas)
admin.site.register(PerfilUsuario)
admin.site.register(Factura)