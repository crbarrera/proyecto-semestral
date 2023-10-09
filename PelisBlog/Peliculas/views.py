from django.shortcuts import render, get_object_or_404
from Peliculas.models import Peliculas
# Create your views here.

def lista_peliculas(request):
    peliculas = Peliculas.objects.all()
    return render(request, 'peliculas.html', {'peliculas':peliculas})

def ficha_pelicula(request, id):
    pelicula = Peliculas.objects.get(id=id)
    return render(request, 'ficha_pelicula.html', {'pelicula':pelicula})