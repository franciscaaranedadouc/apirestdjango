# api/views.py
from rest_framework import viewsets
from .models import (
    InicioCategoria, InicioComuna, InicioMarca, InicioDetalle,
    InicioDireccion, InicioModelo, InicioProducto, InicioRegion,
    InicioTipoprod, InicioTipousuario, InicioUsuario, InicioVenta
)
from .serializers import (
    CategoriaSerializer, ComunaSerializer, MarcaSerializer, DetalleSerializer,
    DireccionSerializer, ModeloSerializer, ProductoSerializer, RegionSerializer,
    TipoProdSerializer, TipoUsuarioSerializer, UsuarioSerializer, VentaSerializer
)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = InicioCategoria.objects.all()
    serializer_class = CategoriaSerializer

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = InicioComuna.objects.all()
    serializer_class = ComunaSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = InicioMarca.objects.all()
    serializer_class = MarcaSerializer

class DetalleViewSet(viewsets.ModelViewSet):
    queryset = InicioDetalle.objects.all()
    serializer_class = DetalleSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = InicioDireccion.objects.all()
    serializer_class = DireccionSerializer

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = InicioModelo.objects.all()
    serializer_class = ModeloSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = InicioProducto.objects.all()
    serializer_class = ProductoSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = InicioRegion.objects.all()
    serializer_class = RegionSerializer

class TipoProdViewSet(viewsets.ModelViewSet):
    queryset = InicioTipoprod.objects.all()
    serializer_class = TipoProdSerializer

class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = InicioTipousuario.objects.all()
    serializer_class = TipoUsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = InicioUsuario.objects.all()
    serializer_class = UsuarioSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = InicioVenta.objects.all()
    serializer_class = VentaSerializer
