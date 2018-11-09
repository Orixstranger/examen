from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse
# Create your views here.
from . forms import FormularioLogin

def logionPage(request):
    if request.method == 'POST':
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']
            user = authenticate(username=usuario,password=clave)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.warning(request, 'Te has identificado de forma correcta')
                    return HttpResponseRedirect(reverse('estudiantes'))
                else:
                    messages.warning(request, 'Usuario inactivo')
            else:
                messages.warning(request, 'Usuario y/o contraseña inactivo')
    else:
        formulario = FormularioLogin()

    context = {
        'f': formulario,
    }
    return render(request, 'login/login.html', context)

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))