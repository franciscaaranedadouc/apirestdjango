from django.urls import path
from .views import inicio, microfono, mouse,registrar_m, registrarse,iniciar

urlpatterns = [
    path('', inicio, name="inicio"),
    path('microfono/', microfono,name="microfono"),
    path('mouse/', mouse,name="mouse"),
    path('registrar/',registrar_m,name="registrar"),
    path('registrarse/',registrarse,name="registrarse"),
    path('iniciar',iniciar,name="iniciar"),
    path('iniciarse',iniciar,name ="iniciarse"),
   
]