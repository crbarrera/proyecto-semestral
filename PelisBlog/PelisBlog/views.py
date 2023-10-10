
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistroForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroForm
from django.contrib.auth.models import User
from django.contrib import messages
from Peliculas.models import PerfilUsuario

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
            PerfilUsuario.objects.update_or_create(user=user,direccion=direccion,telefono=telefono,comuna=comuna,region=region)
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