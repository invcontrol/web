from .models import Item, Proveedor, TipoUnidad, Alerta,Venta,DetalleVenta
from rest_framework import serializers

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['sku','nombre','cantidad','proveedor','cantidad','tipo','precio','alerta_bajo','alerta_sobre']

class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['nombre','telefono','direccion','correo']

class TipoUnidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoUnidad
        fields = ['tipo','abr','cssclass']

class AlertaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alerta
        fields = ['sku','nivel_bajo','nivel_sobre']

class VentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Venta
        fields = ['id','fecha','total']

class DetalleVentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= DetalleVenta
        fields = ['id','cant','precio','venta_id','item_id']