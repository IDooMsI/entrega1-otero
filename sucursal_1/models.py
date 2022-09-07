from statistics import mode
from django.db import models

class Producto(models.Model):
    cantidad = models.IntegerField()
    precio = models.FloatField()
    descripcion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=50)

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    tipo_de_usuario = models.IntegerField()
    sexo = models.CharField(max_length=40)

class TipoDeUsuario(models.Model):
    tipo =  models.CharField(max_length=40)
    descripcion = models.CharField(max_length=255)