from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *

def index(request):
    return render(request,'webpage/index.html')

def control(request):
    if request.method == "POST":
        post = request.POST
        proveedores = Proveedor.objects.all()
        btn = ''
        prod = Item()
        if 'btn-guardar' in post:
            pp = Item.objects.get(sku=post["c-sku"])
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
            prov = post["txtProv"] #cambiar por un select
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
            btn = 'eliminar'
        if 'sel-prod' in post:
            prod = Item.objects.get(sku=post["sel-prod"])
        productos = Item.objects.all()
        return render(request, 'webpage/control.html',{'productos': productos,'prod':prod,'proveedores':proveedores})
    else:
        productos = Item.objects.all()
        return render(request,'webpage/control.html',{'productos': productos,'proveedores':proveedores})

def ingreso(request):
    return render(request, 'webpage/ingreso.html')

def retiro(request):
    return render(request,'webpage/retiro.html')