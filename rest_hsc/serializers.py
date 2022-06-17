from rest_framework import serializers
from Inicio.models import Usuario,Producto,Marca

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username','contrasennia','nombre','apellido','email','tipousuario']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields= ['idProducto','nombreProducto','precioProducto','especificacionProd','stockProd','tipoprod','marca']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Marca
        fields=['idMarca','nombreMarca']