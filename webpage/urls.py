from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('control',views.control, name='control'),
    path('control/retiro',views.retiro,name='retiro'),
    path('control/ingreso',views.ingreso, name='ingreso'),
    path('control/proveedor/new',views.newproveedor,name='agregaproveedor'),
    path('control/proveedor/<int:id>',views.modproveedor,name='modificaproveedor'),
    path('control/unidades/new',views.newunidades,name='newunidad'),
    path('control/unidades/<int:id>',views.modunidades,name='modunidad'),
    path('reportes/completo',views.reporte,name='reporte'),
    path('venta',views.venta,name='venta')
]

