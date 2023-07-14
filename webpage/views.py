from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from .forms import ProveedorForm
from chartkick.django import PieChart, BarChart
from datetime import date

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
        alerta = Alerta()
        if 'btn-mod-prov' in post:
            prov = Proveedor.objects.get(id=post["sel-prov"])
            return redirect('modificaproveedor',prov.id)
        elif 'btn-mod-un' in post:
            un = TipoUnidad.objects.get(id=post["sel-tipo"])
            return redirect('modunidad',un.id)
        elif 'btn-guardar' in post:
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
            precio = post["txtPrecio"]
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
            pp[0].precio = precio
            pp[0].save()
            alerta = Alerta.objects.get_or_create(sku=sku)[0]
            alerta.nivel_bajo=int(post["txtBajoStock"])
            alerta.nivel_sobre=int(post["txtSobreStock"])
            alerta.save()
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
            alerta = Alerta.objects.get(sku=prod.sku)
        elif 'btn-buscar' in post:
            prod = Item.objects.get(sku=post["c-sku"])
        elif 'btn-limpiar' in post:
            return render(request,'webpage/control.html',{'productos': productos,'proveedores':proveedores,'tipos':tipos,'resp':resp,'resp_tipo':resp_tipo})
        return render(request, 'webpage/control.html',{'productos': productos,'prod':prod,'alerta':alerta,'proveedores':proveedores,'tipos':tipos,'resp':resp,'resp_tipo':resp_tipo})
    else:
        return render(request,'webpage/control.html',{'productos': productos,'proveedores':proveedores,'tipos':tipos,'resp':resp,'resp_tipo':resp_tipo})

def ingreso(request):
    if request.method == "POST":
        if 'btn-guardar' in request.POST:
            productos = []
            for key,value in request.POST.items():
                if key.startswith("in-"):
                    sku = key[3:]
                    prod = Item.objects.get(sku=sku)
                    cant = int(value)
                    productos.append([prod,cant])
            for p in productos:
                p[0].cantidad = p[0].cantidad + p[1]
                p[0].save()
            resp = "Actualizacion Hecha"
            resp_tipo = "bg-success"
            return render(request,'webpage/ingreso.html',{'resp':resp,'resp_tipo':resp_tipo})
    else:
        return render(request,'webpage/ingreso.html')

def retiro(request):
    if request.method == "POST":
        if 'btn-guardar' in request.POST:
            productos = []
            for key,value in request.POST.items():
                if key.startswith("in-"):
                    sku = key[3:]
                    prod = Item.objects.get(sku=sku)
                    cant = int(value)
                    productos.append([prod,cant])
            for p in productos:
                p[0].cantidad = p[0].cantidad - p[1]
                p[0].save()
            resp = "Actualizacion Hecha"
            resp_tipo = "bg-success"
            return render(request,'webpage/retiro.html',{'resp':resp,'resp_tipo':resp_tipo})
    else:
        return render(request,'webpage/retiro.html')

def newproveedor(request):
    if 'btn-volver' in request.POST:
        return redirect('control')
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('control')
    else:
        form = ProveedorForm()
        return render(request,'webpage/agregaproveedor.html',{'form':form})

def modproveedor(request,id):
    if 'btn-volver' in request.POST:
        return redirect('control')
    prov = get_object_or_404(Proveedor, id=id)
    if 'btn-eliminar' in request.POST:
        prov.delete()
        return redirect('control')
    return render(request,'webpage/agregaproveedor.html',{'prov':prov})

def newunidades(request):
    return render(request,'webpage/unidades.html')

def modunidades(request,id):
    return render(request,'webpage/unidades.html')

def reporte(request):
    barchart = BarChart({'Work': 32, 'Play': 1492}, width='300px',height='300px')
    piechart = PieChart({'Blueberry': 44, 'Strawberry': 23}, width='300px',height='300px')
    return render(request,'webpage/reporte.html', {'piechart': piechart,'barchart':barchart})

def venta(request):
    if request.method == "POST":
        if 'btn-venta' in request.POST:
            productos = []
            for key,value in request.POST.items():
                if key.startswith("in-"):
                    sku = key[3:]
                    prod = Item.objects.get(sku=sku)
                    cant = int(value)
                    productos.append([prod,cant])
            vta = Venta.objects.get_or_create(id=int(request.POST["numvta"]))[0]
            vta.fecha = date.today()
            vta.total = int(request.POST["total-h"])
            vta.save()
            for p in productos:
                p[0].cantidad = p[0].cantidad - p[1]
                p[0].save()
                dte = DetalleVenta.objects.create(venta=vta,item=p[0],cant=p[1],precio=p[0].precio)
                dte.save()
            
            resp = "Actualizacion Hecha"
            resp_tipo = "bg-success"
            numero = Venta.objects.count() + 1
            return render(request,'webpage/venta.html',{'resp':resp,'resp_tipo':resp_tipo,'numvta':numero})
    
    numero = Venta.objects.count() + 1
    return render(request,'webpage/venta.html',{'numvta':numero})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('sku')
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'sku'

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all().order_by('nombre')
    serializer_class = ProveedorSerializer
    permission_classes = [permissions.IsAuthenticated]

class TipoUnidadViewSet(viewsets.ModelViewSet):
    queryset = TipoUnidad.objects.all().order_by('id')
    serializer_class = TipoUnidadSerializer
    permission_classes = [permissions.IsAuthenticated]

class AlertaViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all().order_by('sku')
    serializer_class = AlertaSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'sku'

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all().order_by('id')
    serializer_class = VentaSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all().order_by('venta_id')
    serializer_class = DetalleVentaSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'venta_id'