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
    tipo = models.ForeignKey('TipoUnidad',on_delete=models.DO_NOTHING, default=1)
    descripcion = models.TextField(max_length=200)
    alerta_bajo = models.BooleanField(default=False)
    alerta_sobre = models.BooleanField(default=False)
    proveedor = models.ForeignKey('Proveedor',on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

class Proveedor(models.Model):
    nombre = models.TextField(max_length=50,null=False)
    telefono = models.IntegerField(null=False)
    correo = models.TextField(max_length=50)
    direccion = models.TextField(null=False)

    def __str__(self):
        return self.nombre


class Alerta(models.Model):
    sku = models.ForeignKey('Item',on_delete=models.CASCADE)
    nivel_bajo = models.IntegerField()
    nivel_sobre = models.IntegerField()


class TipoUnidad(models.Model):
    tipo = models.TextField(null=False)
    abr = models.CharField(max_length=3,null=False)
    
    def __str__(self):
        return self.abr