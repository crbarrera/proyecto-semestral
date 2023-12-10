
from datetime import date, datetime, timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from weasyprint import HTML
from .forms import LoginForm, RegistroForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroForm
from django.contrib.auth.models import User
from django.contrib import messages
from Peliculas.models import PerfilUsuario, Factura
from django.template.loader import get_template

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

def reportes(request):
    data = {
        'facturas': Factura.objects.all()
    }
    return render(request, 'reporte.html', data)

def exportar_reporte_completo(request):

    template_path = 'registro_completo.html'
    context = {
        'facturas': Factura.objects.all()
    }

    response = HttpResponse(content_type='application/informe.pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    HTML(string=html, base_url=request.build_absolute_uri('/')).write_pdf(response)

    return response

# def exportar_reporte_fecha(request):
#     filtro = request.POST.get('filtro')
#     fecha_a_convertir = datetime.strptime(filtro, '%Y-%m-%d')
#     fecha_formateada = fecha_a_convertir.strftime('%Y-%m-%d')

#     template_path = 'registro_completo.html'

#     context = {
#         'facturas': Factura.objects.all().filter(fecha_factura = fecha_formateada)
#     }

#     response = HttpResponse(content_type='application/informe.pdf')
#     response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

#     template = get_template(template_path)
#     html = template.render(context)

#     HTML(string=html, base_url=request.build_absolute_uri('/')).write_pdf(response)

#     return response

def exportar_reporte_fecha(request):
    filtro = request.POST.get('filtro')
    # Agrega el componente del día ('-01') a la cadena de fecha
    fecha_a_convertir = datetime.strptime(filtro + '-01', '%Y-%m-%d')
    fecha_formateada = fecha_a_convertir.strftime('%Y-%m-%d')

    template_path = 'registro_completo.html'

    context = {
        'facturas': Factura.objects.filter(
            fecha_factura__year=fecha_a_convertir.year,
            fecha_factura__month=fecha_a_convertir.month
        )
    }

    response = HttpResponse(content_type='application/informe.pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    HTML(string=html, base_url=request.build_absolute_uri('/')).write_pdf(response)

    return