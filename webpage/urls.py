from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('control',views.control, name='control'),
    path('control/retiro',views.retiro,name='retiro'),
    path('control/ingreso',views.ingreso, name='ingreso'),
    path('control/proveedor',views.proveedor,name='agregaproveedor')
]

