from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.CharField(max_length = 40)
    rut = models.CharField(max_length = 20, primary_key=True)
    nombre = models.CharField(max_length = 30)
    fecha_nacimiento = models.DateField()
    numero_telefono = models.IntegerField()
    region = models.CharField(max_length = 60)
    comuna = models.CharField(max_length = 60)
    tipo_casa = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

class Rescatado(models.Model):
    foto = models.ImageField(upload_to='rescatados/')
    nombre = models.CharField(max_length = 30)
    raza = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 30)
    state = models.CharField(max_length=15)


