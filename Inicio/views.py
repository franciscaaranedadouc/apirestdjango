from django.shortcuts import render,redirect
from .models import Usuario,Direccion,Comuna,Region,TipoUsuario, Producto, Marca,Categoria,TipoProd,Marca
from django.contrib import messages
import os 

# Create your views here.
def inicio(request):

    return render(request,'Inicio/index.html')
def inicioadmin(request):

    return render(request,'Inicio/index_admin.html') 
def vistamod(request):
    
    return render(request,'Inicio/modificar_producto.html')


def addprod (request):
    tipoProd = TipoProd.objects.all()
    marca = Marca.objects.all()
    contexto = {"tipoProd":tipoProd,"Marca":marca}

    return render (request,'Inicio/agregar_producto.html',contexto)   

def iniciar(request):

    return render(request,'Inicio/inicio_sesion.html')

def menuadmin(request):

    return render(request,'Inicio/dashboard-admin.html')

def carrito(request):

    return render(request,'Inicio/carrito.html')


# -------------------- PRODUCTOS --------------------
# MICROFONOS
def mostrarMic(request):
    micros = Producto.objects.filter(tipoprod=1)
    return render(request, "Inicio/microfonos.html",{"mic": micros})

def micadmin (request):
    micros = Producto.objects.filter(tipoprod=1)
    return render (request,'Inicio/micadmin.html',{"mic": micros}) 
    
def micro(request,id):
    productos = Producto.objects.get(idProducto = id)
    return render(request, "Inicio/mic1.html",{"prod": productos})    



# TECLADOS
def mostrarTeclado(request):
    teclados = Producto.objects.filter(tipoprod=2)
    return render(request, "Inicio/teclados.html",{"teclado": teclados})

def tecladoadmin (request):
    teclados = Producto.objects.filter(tipoprod=2)
    return render (request,'Inicio/tecladoadmin.html',{"teclado": teclados}) 

def teclado(request,id):
    productos = Producto.objects.get(idProducto = id)
    return render(request, "Inicio/mic1.html",{"prod": productos})



# GRAFICAS
def mostrarGrafica(request):
    graficas = Producto.objects.filter(tipoprod=3)
    return render(request, "Inicio/graficas.html",{"grafica": graficas})

def graficaAdmin (request):
    graficas= Producto.objects.filter(tipoprod=3)
    return render (request,'Inicio/graficaAdmin.html',{"grafica": graficas}) 
    
def grafica(request,id):
    productos = Producto.objects.get(idProducto = id)
    return render(request, "Inicio/mic1.html",{"prod": productos})    



# RAMS
def mostrarRam(request):
    rams = Producto.objects.filter(tipoprod=4)
    return render(request, "Inicio/rams.html",{"ram": rams})

def ramAdmin (request):
    rams= Producto.objects.filter(tipoprod=4)
    return render (request,'Inicio/ramAdmin.html',{"ram": rams}) 
    
def ram(request,id):
    productos = Producto.objects.get(idProducto = id)
    return render(request, "Inicio/mic1.html",{"prod": productos})    



# MOUSES
def mostrarMouse(request):
    mouses = Producto.objects.filter(tipoprod=5)
    return render(request, "Inicio/mouses.html",{"mouse": mouses})

def mouseAdmin (request):
    mouses= Producto.objects.filter(tipoprod=5)
    return render (request,'Inicio/mouseAdmin.html',{"mouse": mouses}) 
    
def mouse(request,id):
    productos = Producto.objects.get(idProducto = id)
    return render(request, "Inicio/mic1.html",{"prod": productos})    



# PROCESADORES
def mostrarProcesador(request):
    procesadores = Producto.objects.filter(tipoprod=6)
    return render(request, "Inicio/procesadores.html",{"procesador": procesadores})

def procesadorAdmin (request):
    procesadores= Producto.objects.filter(tipoprod=6)
    return render (request,'Inicio/procesadorAdmin.html',{"procesador": procesadores}) 
    
def procesador(request,id):
    productos = Producto.objects.get(idProducto = id)
    return render(request, "Inicio/mic1.html",{"prod": productos})  



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
            contexto = {"usuario":usuario2}

           
            return render(request, 'Inicio/index.html', contexto)
            


    except:
        messages.error(request,'El usuario o la contraseña son incorrectos')
        return redirect ('iniciar')
    

    
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
    

def eliminarProducto(request, idProducto):
    producto= Producto.objects.get(idProducto=idProducto)
    producto.delete()

    messages.success(request, '¡Producto Eliminado!')

    return redirect('indexadmin')


 
def edicionProducto(request, idProducto):
    tipoProd = TipoProd.objects.all()
    marca = Marca.objects.all()
    producto = Producto.objects.get(idProducto=idProducto)

    return render(request,'Inicio/edicionProducto.html', {"producto": producto, "tipoProd":tipoProd,"Marca":marca})

def editarProducto(request,idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    tiprod1 =request.POST['tipoprod'] 
    tipoprod2 = TipoProd.objects.get(idTiporod =tiprod1)
    marca1 = request.POST['marcaprod']
    marca2 = Marca.objects.get(idMarca = marca1)
    if (request.FILES.get("imgprod")):
        fotoprod =  request.FILES['imgprod']
        producto.imagenProd = fotoprod
    producto.nombreProducto = request.POST.get('nomprod')
    producto.tipoprod = tipoprod2
    producto.marca = marca2
    producto.stockProd = request.POST.get('stockprod')
    producto.precioProducto = request.POST.get('precio')
    producto.especificacionProd = request.POST.get('descprod')
    producto.save()
    messages.success(request, '¡Producto Modificado!')
    return redirect('indexadmin')

