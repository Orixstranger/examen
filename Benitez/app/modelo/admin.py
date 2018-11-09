from django.contrib import admin

from .models import Estudiante
# Register your models here.
class AdminEstudiante(admin.ModelAdmin):
    list_display = ["cedula", "codigo_matricula", "nombres", "apellidos", "carrera", "ciclo","estado"]
    list_editable = ["nombres","apellidos"]
    list_filter = ["carrera", "ciclo"]
    search_fields = ["cedula"], "nombres","apellidos"

    class Meta:
        model = Estudiante
admin.site.register(Estudiante,AdminEstudiante)