
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegistroForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroForm
from django.contrib.auth.models import User
from django.contrib import messages
from Peliculas.models import PerfilUsuario, Factura

def index(request):
    return render(request, "index.html")

def peliculas(request):
    return render(request, "peliculas.html")

def login_succes(request):
    data = {"mesg": "", "form": LoginForm()}

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(to='inicio')
                else:
                    data["mesg"] = "¡Nombre de usuario o contraseña no son correctos!"
            else:
                data["mesg"] = "¡Nombre de usuario o contraseña no son correctos!"
    return render(request, 'login.html', data)

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            direccion = request.POST.get("direccion")
            telefono = request.POST.get("telefono")
            comuna = request.POST.get("comuna")
            region = request.POST.get("region")
            rut = request.POST.get("rut")
            PerfilUsuario.objects.update_or_create(user=user,direccion=direccion,telefono=telefono,comuna=comuna,region=region, rut=rut)
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            print(direccion)
            return redirect('login')
        else:
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
    else:
        form = RegistroForm()
    form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def logout_succes(request):
    logout(request)
    # Redirige al usuario a la página de inicio de sesión o a cualquier otra página que desees.
    return redirect('inicio')

def compras(request):
    persona = PerfilUsuario.objects.all()
    return render(request, 'compras.html', {'persona':persona})

def orden_de_compra(request, id):
    factura = Factura.objects.filter(codigo_factura = id)
    
    datos_factura = Factura.objects.get(codigo_factura = id)
    
    precio = datos_factura.precio_producto
    cantidad = datos_factura.monto_producto
    estado_factura = datos_factura.estado_factura
    
    monto_neto = int(precio*cantidad)
    monto_iva = int(monto_neto*0.19)
    monto_total = int(monto_neto+monto_iva)
    return render(request, 'orden_de_compra.html', {'factura': factura, 'monto_neto':monto_neto, 'monto_iva':monto_iva, 'monto_total':monto_total, 'estado_factura': estado_factura})

def ordenes_de_compras(request):
    factura = Factura.objects.all()
    if request.method == "POST":
        valor_id = request.POST['factura_id']
        print("--------------------------------------")
        print(valor_id)
        print("--------------------------------------")
        factura_cambio = request.POST['estado']
        
        obtener_factura = get_object_or_404(Factura, pk=valor_id)
        obtener_factura.estado_factura = factura_cambio
        
        obtener_factura.save()
    return render(request, 'ordenes_de_compras.html', {'factura':factura})

def perfil(request):
    usuario = request.user
    
    perfil = PerfilUsuario.objects.get(user=usuario)
    facturas = Factura.objects.filter(usuario=perfil)
    return render(request, 'perfil_de_usuario.html', {'perfil':perfil, 'facturas': facturas})