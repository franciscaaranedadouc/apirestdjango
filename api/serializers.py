# api/serializers.py
from rest_framework import serializers
from .models import (
    InicioCategoria,
    InicioComuna,
    InicioMarca,
    InicioDetalle,
    InicioDireccion,
    InicioModelo,
    InicioProducto,
    InicioRegion,
    InicioTipoprod,
    InicioTipousuario,
    InicioUsuario,
    InicioVenta
)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioCategoria
        fields = '__all__'

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioComuna
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioMarca
        fields = '__all__'

class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioDetalle
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioDireccion
        fields = '__all__'

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioModelo
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioProducto
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioRegion
        fields = '__all__'

class TipoProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioTipoprod
        fields = '__all__'

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioTipousuario
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioUsuario
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioVenta
        fields = '__all__'
