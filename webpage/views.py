from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from .models import *

def index(request):
    return render(request,'webpage/index.html')

def control(request):
    proveedores = Proveedor.objects.all()
    productos = Item.objects.all()
    tipos = TipoUnidad.objects.all()
    if request.method == "POST":
        post = request.POST
        prod = Item()
        resp = ""
        if 'btn-guardar' in post:
            pp = Item.objects.get_or_create(id=post["id"])
            pp = pp[0]
            sku = post["c-sku"]
            nombre = post["txtNombre"]
            cantidad = post["txtCantidad"]
            tipo = post["sel-tipo"]
            desc = post["txtDesc"]
            bajostock = ""
            sobrestock = ""
            if "bajoStockCheck" in post:
                bajostock = post["bajoStockCheck"]
            if "sobreStockCheck" in post:
                sobrestock = post["sobreStockCheck"]
            prov = Proveedor.objects.get(id=post["sel-prov"])
            pp.sku = sku
            pp.nombre = nombre
            pp.cantidad = cantidad
            pp.descripcion = desc
            pp.tipo = TipoUnidad.objects.get(id=tipo)
            pp.proveedor = Proveedor.objects.get(nombre=prov)
            if bajostock == "on":
                pp.alerta_bajo = True
            else:
                pp.alerta_bajo = False
            if sobrestock == "on":
                pp.alerta_sobre = True
            else:
                pp.alerta_sobre = False
            pp.save()
        elif 'btn-eliminar' in post:
            try:
                pp = Item.objects.get(id=post["id"])
                pp.delete()
                return render(request,'webpage/control.html',{'productos': productos,'proveedores':proveedores,'tipos':tipos})
            except ObjectDoesNotExist:
                resp = "No existe el Producto"
        elif 'sel-prod' in post:
            prod = Item.objects.get(sku=post["sel-prod"])
        elif 'btn-buscar' in post:
            prod = Item.objects.get(sku=post["c-sku"])
        elif 'btn-limpiar' in post:
            return render(request,'webpage/control.html',{'productos': productos,'proveedores':proveedores,'tipos':tipos})
        return render(request, 'webpage/control.html',{'productos': productos,'prod':prod,'proveedores':proveedores,'tipos':tipos})
    else:
        return render(request,'webpage/control.html',{'productos': productos,'proveedores':proveedores,'tipos':tipos})

def ingreso(request):
    return render(request, 'webpage/ingreso.html')

def retiro(request):
    return render(request,'webpage/retiro.html')