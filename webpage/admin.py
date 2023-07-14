from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Item)
admin.site.register(Proveedor)
admin.site.register(Alerta)
admin.site.register(TipoUnidad)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(RegistroMovimientos)
admin.site.register(TipoMovimiento)