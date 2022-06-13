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
    resp = ""
    resp_tipo = ""
    if request.method == "POST":
        post = request.POST
        prod = Item()
        if 'btn-guardar' in post:
            pp = Item()
            if post["id"] != '':
                pp = Item.objects.get_or_create(id=post["id"])
            else:
                pp = Item.objects.get_or_create(sku=post["c-sku"])
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
            pp[0].sku = sku
            pp[0].nombre = nombre
            pp[0].cantidad = cantidad
            pp[0].descripcion = desc
            pp[0].tipo = TipoUnidad.objects.get(id=tipo)
            pp[0].proveedor = Proveedor.objects.get(nombre=prov)
            pp[0].alerta_bajo = True if bajostock == "on" else False
            pp[0].alerta_sobre = True if sobrestock == "on" else False
            pp[0].save()
            resp = "Producto Creado" if pp[1] else "Producto Modificado"
            resp_tipo = "bg-success"
            return render(request,'webpage/control.html',{'productos': productos,'proveedores':proveedores,'tipos':tipos,'resp':resp,'resp_tipo':resp_tipo})
        elif 'btn-eliminar' in post:
            try:
                pp = Item.objects.get(id=post["id"])
                pp.delete()
            except:
                resp = "No existe el Producto"
                resp_tipo = "bg-danger"
            return render(request,'webpage/control.html',{'productos': productos,'proveedores':proveedores,'tipos':tipos,'resp':resp,'resp_tipo':resp_tipo})
        elif 'sel-prod' in post:
            prod = Item.objects.get(sku=post["sel-prod"])
        elif 'btn-buscar' in post:
            prod = Item.objects.get(sku=post["c-sku"])
        elif 'btn-limpiar' in post:
            return render(request,'webpage/control.html',{'productos': productos,'proveedores':proveedores,'tipos':tipos,'resp':resp,'resp_tipo':resp_tipo})
        return render(request, 'webpage/control.html',{'productos': productos,'prod':prod,'proveedores':proveedores,'tipos':tipos,'resp':resp,'resp_tipo':resp_tipo})
    else:
        return render(request,'webpage/control.html',{'productos': productos,'proveedores':proveedores,'tipos':tipos,'resp':resp,'resp_tipo':resp_tipo})

def ingreso(request):
    return render(request, 'webpage/ingreso.html')

def retiro(request):
    return render(request,'webpage/retiro.html')