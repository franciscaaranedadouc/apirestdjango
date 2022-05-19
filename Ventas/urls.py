from django.urls import path
from .views import inicio, home,mascota, mascota2,listado,formulario

urlpatterns = [
    path('', inicio, name="inicio"),
    path('home/', home, name="home"),
    path('mascota/',mascota,name="mascota"),
    path('mascota2/',mascota2, name="mascota2"),
    path('listado/',listado,name="listado"),
    path('formulario/',formulario,name="formulario"),
]