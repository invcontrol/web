from .models import Item, Proveedor, TipoUnidad
from rest_framework import serializers

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['sku','nombre','cantidad','proveedor','cantidad','tipo']

class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['nombre','telefono','direccion','correo']

class TipoUnidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoUnidad
        fields = ['tipo','abr']