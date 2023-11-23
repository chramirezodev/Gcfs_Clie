from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def inicio(request):
    # Comprueba si estás iniciando sesión
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Autenticar
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request, "¡Has iniciado sesión!")
            return redirect('inicio')
        else:
            messages.success(request, "Se ha producido un error al iniciar sesión, inténtalo de nuevo...")
            return redirect('inicio')
    else:
        return render(request, 'inicio.html', {})

#def login_user(request):
    #pass

def logout_user(request):
    logout(request)
    messages.success(request,"¡Has sido desconectado!..." )
    return redirect('inicio')


def register_user(request):
    return render (request, 'register.html', {})
# Create your views here.
