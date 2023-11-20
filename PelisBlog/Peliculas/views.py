from django.shortcuts import render, get_object_or_404, redirect
from Peliculas.models import Peliculas, PerfilUsuario, Factura

# Create your views here.

def lista_peliculas(request):
    peliculas = Peliculas.objects.all()
    return render(request, 'peliculas.html', {'peliculas':peliculas})

def ficha_pelicula(request, id):
    
    pelicula = Peliculas.objects.get(id=id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if not request.user.is_staff:
                user = request.user
                
                perfil = PerfilUsuario.objects.get(user=user)
                
                usuario = perfil
                
                nombre_pelicula = pelicula.nombre
                precio_pelicula = pelicula.precio
                cantidad_pelicula = request.POST['cantidad']
                
                factura = Factura.objects.create(usuario=usuario, nombre_producto=nombre_pelicula, monto_producto=cantidad_pelicula, precio_producto=precio_pelicula)
                return redirect ('orden_de_compra', factura.pk)
            else:
                return redirect ('ficha_pelicula', id = pelicula.pk)
        else:
            return redirect ('ficha_pelicula', id = pelicula.pk)
            
    return render(request, 'ficha_pelicula.html', {'pelicula':pelicula})

def compra_exitosa(request):
    return render(request, 'compra_exitosa.html')

def compras(request):
    persona = PerfilUsuario.objects.all()
    if request.method == "POST":
        valor_id = request.POST['factura_id']
        factura_cambio = request.POST['estado']
        
        obtener_factura = get_object_or_404(Factura, pk=valor_id)
        obtener_factura.estado_factura = factura_cambio
        
        obtener_factura.save()
    return render(request, 'compras.html', {'persona':persona})

