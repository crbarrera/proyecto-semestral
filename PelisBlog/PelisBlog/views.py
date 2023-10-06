from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def peliculas(request):
    return render(request, "peliculas.html")