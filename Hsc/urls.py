"""Hsc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    CategoriaViewSet, ComunaViewSet, MarcaViewSet, DetalleViewSet,
    DireccionViewSet, ModeloViewSet, ProductoViewSet, RegionViewSet,
    TipoProdViewSet, TipoUsuarioViewSet, UsuarioViewSet, VentaViewSet
)

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'comunas', ComunaViewSet, basename='comuna')
router.register(r'marcas', MarcaViewSet, basename='marca')
router.register(r'detalles', DetalleViewSet, basename='detalle')
router.register(r'direcciones', DireccionViewSet, basename='direccion')
router.register(r'modelos', ModeloViewSet, basename='modelo')
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'regiones', RegionViewSet, basename='region')
router.register(r'tipoprod', TipoProdViewSet, basename='tipoprod')
router.register(r'tipousuarios', TipoUsuarioViewSet, basename='tipousuario')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'ventas', VentaViewSet, basename='venta')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Inicio.urls')),
    path('api/', include(router.urls)),
]

