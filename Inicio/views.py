from django.shortcuts import render,redirect
from .models import Usuario,Direccion,Comuna,Region,TipoUsuario, Producto, Marca, Modelo, Categoria,TipoProd,Marca
from django.contrib import messages

# Create your views here.
def inicio(request):

    return render(request,'Inicio/index.html')


def iniciar(request):

    return render(request,'Inicio/inicio_sesion.html')

def menuadmin(request):

    return render(request,'Inicio/dashboard-admin.html')

def addprod (request):
    tipoProd = TipoProd.objects.all()
    marca = Marca.objects.all()
    contexto = {"tipoProd":tipoProd,"Marca":marca}

    return render (request,'Inicio/agregar_producto.html',contexto)

def mostrarMic(request):
    micros = Producto.objects.all()
    return render(request, "Inicio/microfonos.html",{"mic": micros})

def registrarse(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    contexto = {"comunas_m": comunas,"regiones_m": regiones}
    return render(request,"Inicio/registrarse.html",contexto)

def registrar_m (request):
    user = request.POST['usuario']
    contra = request.POST['contra']
    correo = request.POST['email']
    region = request.POST['region']
    direccion = request.POST['direccion']
    comuna = request.POST['comuna']
    nombree = request.POST['nombre']
    apellido = request.POST['apellido']
    
    comuna2 = Comuna.objects.get(idComuna = comuna)
    region2 = Region.objects.get(idRegion = region)
    tipousuario2 = TipoUsuario.objects.get(idTipoUsuario = 2)
    existe = None
    try:
        existe = Usuario.objects.get(username=user)
        messages.error(request,'El usuario ya existe')
        return redirect ('registrarse')
    except:
        Usuario.objects.create(username = user , contrasennia = contra, nombre = nombree, apellido = apellido, email = correo,tipousuario = tipousuario2)
        x = Usuario.objects.get(username = user)
        Direccion.objects.create(descripcionDir = direccion, usuario = x,region = region2)
        return redirect ('iniciar')





def iniciar_sesion(request):
    usuario1 = request.POST['usuario']
    contra1 = request.POST['contra']
    try:
        usuario2 = Usuario.objects.get(username = usuario1,contrasennia = contra1)

        if(usuario2.tipousuario.idTipoUsuario == 1):
            return redirect ('menu_admin')
        else:               
            return redirect ('inicio')


    except:
        messages.error(request,'El usuario o la contraseña son incorrectos')
        return redirect ('iniciar')
    
def micro(request,id):
    productos = Producto.objects.get(idProducto = id)
    return render(request, "Inicio/mic1.html",{"prod": productos})
    
def newProd(request):
    nombre = request.POST['nomprod']
    tipoProd = request.POST['tipoprod']
    marca = request.POST['marcaprod']
    stock = request.POST['stockprod']
    imagen = request.FILES['imgprod']
    desc = request.POST['descprod']
    precio = request.POST['precio']
    
    idProd2 = TipoProd.objects.get(idTiporod = tipoProd)
    marca2 = Marca.objects.get(idMarca = marca)
    existe = None
    try:
        existe = Producto.objects.get(nombreProducto = nombre)
        messages.error(request,'El producto ya existe')
        return redirect ('addprod')
    except:
        Producto.objects.create(nombreProducto = nombre,precioProducto = precio,especificacionProd = desc,stockProd =stock,imagenProd = imagen,tipoprod = idProd2,marca = marca2)
        return redirect ('menu_admin')
    


    
    