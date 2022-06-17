from django.urls import path
from rest_hsc.views import lista_usuarios,agregarU,controlU

urlpatterns = [
    path('lista_usuarios/',lista_usuarios,name="lista_usuarios"),
    path('agregarU/',agregarU,name="agregarU"),
    path('controlU/<usuario1>',controlU,name="controlU"),

    
]