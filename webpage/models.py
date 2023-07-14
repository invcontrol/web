from contextlib import nullcontext
from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class Item(models.Model):
    sku = models.IntegerField(default=1)
    nombre = models.TextField(default="test")
    cantidad = models.IntegerField(default=1)
    tipo = models.ForeignKey('TipoUnidad',on_delete=models.DO_NOTHING, default=1)
    descripcion = models.TextField(max_length=200, default="item_prueba")
    alerta_bajo = models.BooleanField(default=False)
    alerta_sobre = models.BooleanField(default=False)
    proveedor = models.ForeignKey('Proveedor',on_delete=models.CASCADE, default=1)
    precio = models.IntegerField(default=1)
    def __str__(self):
        return self.nombre
    

class Proveedor(models.Model):
    nombre = models.TextField(max_length=50,null=False)
    telefono = models.IntegerField(null=True)
    correo = models.TextField(max_length=50,null=True)
    direccion = models.TextField(null=True)

    def __str__(self):
        return self.nombre


class Alerta(models.Model):
    sku = models.IntegerField()
    nivel_bajo = models.IntegerField(null=True)
    nivel_sobre = models.IntegerField(null=True)
    def __str__(self):
        return self.id

class TipoUnidad(models.Model):
    tipo = models.TextField(null=False)
    abr = models.CharField(max_length=3,null=False)
    cssclass = models.CharField(max_length=5,default="in-kg")
    def __str__(self):
        return self.abr
    
class RegistroMovimientos(models.Model):
    tipo = models.ForeignKey('TipoMovimiento',on_delete=models.CASCADE)
    sku = models.ForeignKey('Item',on_delete=models.CASCADE)
    fecha = models.DateField()
    stockbf = models.IntegerField()
    stockaf = models.IntegerField()
    preciobf = models.IntegerField()
    precioaf = models.IntegerField()


class TipoMovimiento(models.Model):
    tipo = models.TextField(null=False)
    abr = models.CharField(max_length=3, null=False)
    cssclass = models.CharField(max_length=5)

class Venta(models.Model):
    fecha = models.DateField(default=timezone.now)
    total = models.IntegerField(default=0)

class DetalleVenta(models.Model):
    venta = models.ForeignKey('Venta',on_delete=models.DO_NOTHING)
    item = models.ForeignKey('Item',on_delete=models.DO_NOTHING)
    cant = models.IntegerField(default=1)
    precio = models.IntegerField(default=1)