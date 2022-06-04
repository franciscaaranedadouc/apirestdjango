from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', inicio, name="inicio"),
    path('indexadmin',inicioadmin,name="indexadmin"),

    path('registrar/',registrar_m,name="registrar"),
    path('registrarse/',registrarse,name="registrarse"),
    #Pag agregar producto
    path('agregar2/',newProd,name ="addProd"),
    path('agregar/',addprod,name="agregarprod"),
    #modificar un producto
    path('modificar/',vistamod,name="modificar"),
    path('eliminarProducto/<idProducto>',eliminarProducto,name="eliminarProducto"),

    #Pag menu admin
    path ('menuadmin/',menuadmin,name="menu_admin"),
    path('micadmin/',micadmin,name="micadmin"),
    path('tecladoadmin/',tecladoadmin,name="tecladoadmin"),
    #Pagina iniciar
    path('iniciar/',iniciar,name="iniciar"),
    
    #Valida usuario
    path('iniciarsesion/',iniciar_sesion,name ="iniciarsesion"),
    #Mostrar productos
    path('teclados',mostrarTeclado,name="teclados"),
    path('teclados/<int:id>',teclado, name="teclado"),

    path('microfonos/',mostrarMic, name="mostrarMic"),
    path('microfonos/<int:id>',micro, name="micro"),
    #Carrito
    path('carrito/',carrito, name="carrito"),
    


    path('edicionProducto/<idProducto>', edicionProducto, name="edicionProducto"),
    path('editarProducto/<idProducto>', editarProducto, name="editarProducto"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)