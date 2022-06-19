from django.urls import path
from rest_hsc.views import lista_usuarios,agregarU,controlU, lista_productos, agregarP,controlP,lista_marcas,agregarM,controlM
from rest_hsc.viewsLogin import login

urlpatterns = [
    #Usuarios
    path('lista_usuarios/',lista_usuarios,name="lista_usuarios"),
    path('agregarU/',agregarU,name="agregarU"),
    path('controlU/<usuario1>',controlU,name="controlU"),
    #Productos
    path('lista_productos/',lista_productos,name="lista_productos"),
    path('agregarP/',agregarP,name="agregarP"),
    path('controlP/<idproductos>',controlP,name="controlP"),
    #Marcas
    path('lista_marcas/',lista_marcas,name="lista_marcas"),
    path('agregarM/',agregarM,name="agregarM"),
    path('controlM/<idmarcas>',controlM,name="controlM"),
    path('login/',login,name="login"),


]