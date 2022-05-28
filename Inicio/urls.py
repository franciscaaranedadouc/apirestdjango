from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('microfono/', microfono,name="microfono"),
    path('mouse/', mouse,name="mouse"),
    path('registrar/',registrar_m,name="registrar"),
    path('registrarse/',registrarse,name="registrarse"),
    
    ##Pagina iniciar
    path('iniciar/',iniciar,name="iniciar"),

    ##Valida usuario
    path('iniciarsesion/',iniciar_sesion,name ="iniciarsesion"),
   
]