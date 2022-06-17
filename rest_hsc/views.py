from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import UsuarioSerializer, ProductoSerializer, MarcaSerializer
from Inicio.models import Producto, Usuario, Marca

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

##################################################USUARIOS##################################################
@csrf_exempt

@api_view(['GET', 'POST'])
##@permission_classes((IsAuthenticated,))
def lista_usuarios(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#######################
@api_view(['GET', 'POST'])
##@permission_classes((IsAuthenticated,))
def agregarU(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
##@permission_classes((IsAuthenticated,))
def controlU(request,usuario1):
    try:
        usuario = Usuario.objects.get(username = usuario1)
    except Usuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
##################################################PRODUCTOS##################################################
@api_view(['GET', 'POST'])
##@permission_classes((IsAuthenticated,))
def lista_productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#######################
@api_view(['GET', 'POST'])
##@permission_classes((IsAuthenticated,))
def agregarP(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#######################
@api_view(['GET','PUT','DELETE'])
##@permission_classes((IsAuthenticated,))
def controlP(request,idproductos):
    try:
        productos = Producto.objects.get(idProducto = idproductos)
    except Producto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductoSerializer(productos)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializer(productos,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        productos.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
##################################################MARCA##################################################
@api_view(['GET', 'POST'])
##@permission_classes((IsAuthenticated,))
def lista_marcas(request):
    if request.method == 'GET':
        marcas = Marca.objects.all()
        serializer = MarcaSerializer(marcas,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = MarcaSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#######################
@api_view(['GET', 'POST'])
##@permission_classes((IsAuthenticated,))
def agregarM(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = MarcaSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
##@permission_classes((IsAuthenticated,))
def controlM(request,idmarcas):
    try:
        marcas = Marca.objects.get(idMarca = idmarcas)
    except Marca.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MarcaSerializer(marcas)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = MarcaSerializer(marcas,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        marcas.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        