from rest_framework import serializers
from Inicio.models import Usuario,Producto,Region

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username','contrasennia','nombre','apellido','email','tipousuario']
