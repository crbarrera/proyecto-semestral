
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, logout, authenticate

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

def logout_succes(request):
    logout(request)
    # Redirige al usuario a la página de inicio de sesión o a cualquier otra página que desees.
    return redirect('inicio')