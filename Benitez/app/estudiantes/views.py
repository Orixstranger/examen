from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from app.estudiantes import forms
from .forms import FomularioEstudiante
from app.modelo.models import Estudiante

# Create your views here.
@login_required
def principal(request):
    usuario = request.user
    if usuario.has_perm('modelo.add_estudiante'):
        listaEstudiantes = Estudiante.objects.all().filter(estado=True).order_by('apellidos')
        context = {
            'lista': listaEstudiantes
        }
        return render(request, 'estudiantes/principal_estudiante.html',context)
    else:
        return render(request, 'login/acceso_prohibido.html')


def crear(request):
    formulario = FomularioEstudiante(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            estudiante = Estudiante()
            estudiante.cedula = datos.get('cedula')
            estudiante.codigo_matricula = datos.get('codigo_matricula')
            estudiante.apellidos = datos.get('apellidos')
            estudiante.nombres = datos.get('nombres')
            estudiante.carrera = datos.get('carrera')
            estudiante.ciclo = datos.get('ciclo')
            estudiante.save()
            return redirect(principal)
    context = {
        'f': formulario,
        'mensaje': 'Bienvenido'
    }

    return render(request, 'estudiantes/crear_estudiante.html', context)

def modificar(request):
    dni = request.GET['cedula']
    estudiante = Estudiante.objects.get(cedula = dni )
    formulario = FomularioEstudiante(instance=estudiante)
    if request.method == "POST":
        estudiante.cedula = request.POST['cedula']
        estudiante.codigo_matricula = request.POST['codigo_matricula']
        estudiante.nombres = request.POST['nombres']
        estudiante.apellidos = request.POST['apellidos']
        estudiante.carrera = request.POST['carrera']
        estudiante.ciclo = request.POST['ciclo']
        estudiante.save()
        return redirect(principal)

    return render(request, 'estudiantes/crear_estudiante.html', {
            'f': formulario,
        })

def eliminar(request):
    dni = request.GET['cedula']
    estudiante = Estudiante.objects.get(cedula=dni)
    estudiante.estado = False
    estudiante.save()
    return redirect(principal)