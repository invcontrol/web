from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('Control',views.control, name='control'),
    path('Control/Retiro',views.retiro,name='retiro'),
    path('Control/Ingreso',views.ingreso, name='ingreso'),
    path('Control/Proveedor',views.proveedor,name='agregaproveedor')
]

