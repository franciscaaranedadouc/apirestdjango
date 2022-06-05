from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    #Pagina iniciar/ Solo carga pagina
    path('iniciar/',iniciar,name="iniciar"),
    
    #Valida usuario / Aqui tenemos las consultas
    #Sacamos datos de aqui d1
    path('iniciarsesion/',iniciar_sesion,name ="iniciarsesion"),

    # La pagina principal
    #Metemos datos aqui d1
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
    path('mouseAdmin/',mouseAdmin,name="mouseAdmin"),
    path('ramAdmin/',ramAdmin,name="ramAdmin"),
    path('graficaAdmin/',graficaAdmin,name="graficaAdmin"),
    path('procesadorAdmin/',procesadorAdmin,name="procesadorAdmin"),
    
    #Mostrar productos
    path('teclados',mostrarTeclado,name="teclados"),
    path('teclados/<int:id>',teclado, name="teclado"),

    path('microfonos/',mostrarMic, name="mostrarMic"),
    path('microfonos/<int:id>',micro, name="micro"),

    path('mouses/',mostrarMouse, name="mostrarMouse"),
    path('mouses/<int:id>',mouse, name="mouse"),

    path('graficas/',mostrarGrafica, name="mostrarGrafica"),
    path('graficas/<int:id>',grafica, name="grafica"),

    path('rams/',mostrarRam, name="mostrarRam"),
    path('rams/<int:id>',ram, name="ram"),

    path('procesadores/',mostrarProcesador, name="mostrarProcesador"),
    path('procesadores/<int:id>',procesador, name="procesador"),


    #Carrito
    path('carrito/',carrito, name="carrito"),
    


    path('edicionProducto/<idProducto>', edicionProducto, name="edicionProducto"),
    path('editarProducto/<idProducto>', editarProducto, name="editarProducto"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)