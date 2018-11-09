from django.db import models

# Create your models here.max_length
class Estudiante(models.Model):
    lista_carrera = (
        ('sistemas', 'Sistemas'),
        ('contabilidad', 'Contailidad'),
        ('forestal','Forestal'),
        ('medicina', 'Medicina'),
        ('ingles', 'Ingles')
    )
    lista_ciclo = (
        ('1',"Primer Ciclo"),
        ('2', "Segundo Ciclo"),
        ('3', "Tercer Ciclo"),
        ('4',"Cuarto Ciclo"),
        ('5',"Quinto Ciclo"),
        ('6',"Sexto Ciclo"),
        ('7', "Septimo Ciclo"),
        ('8', "Octavo Ciclo"),
        ('9', "Noveno Ciclo"),
        ('10', "Decimo Ciclo"),

    )
    cedula_id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    codigo_matricula = models.CharField(max_length=8)
    nombres = models.CharField(max_length=70)
    apellidos = models.CharField(max_length=70)
    carrera = models.CharField(max_length=15, choices=lista_carrera,null=False)
    ciclo = models.CharField(max_length=15,choices=lista_ciclo,null=False)
    estado = models.BooleanField(default=True)

