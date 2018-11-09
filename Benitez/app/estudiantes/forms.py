from django import forms
from app.modelo.models import Estudiante

class FomularioEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["codigo_matricula","cedula","nombres","apellidos","carrera","ciclo"]