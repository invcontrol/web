from contextlib import nullcontext
from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    sku = models.IntegerField()
    nombre = models.TextField()
    cantidad = models.IntegerField()
    descripcion = models.TextField(max_length=200)
    alerta_bajo = models.BooleanField(default=False)
    alerta_sobre = models.BooleanField(default=False)
    proveedor = models.ForeignKey('Proveedor',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre
    

class Proveedor(models.Model):
    nombre = models.TextField(max_length=50,null=False)
    telefono = models.IntegerField(null=False)
    correo = models.TextField(max_length=50)
    direccion = models.TextField(null=False)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    correo = models.TextField(null=False, max_length=50)
    nombre = models.TextField(null=False, max_length=50)

    def __str__(self):
        return self.nombre