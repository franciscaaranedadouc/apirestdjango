from django.shortcuts import render,redirect
from .models import Usuario,Direccion,Comuna,Region,TipoUsuario

# Create your views here.
def inicio(request):

    return render(request,'Inicio/index.html')


def microfono(request):
    contexto = {"Titulo": "Micrófonos", "Nombre1": "Razer", "Modelo1": "Seiren Mini", "Precio1": "$47.000", "Imagen1": "/static/Inicio/img/img-micros/seireni.jpg",
    "Nombre2": "Razer", "Modelo2": "Seiren Mini", "Precio2": "$47.000", "Imagen2": "/static/Inicio/img/img-micros/quad.jpg",
    "Nombre3": "Hyper X", "Modelo3": "Quadcast S RGB", "Precio3": "$119.000", "Imagen3": "/static/Inicio/img/img-micros/fifain.jpg",
    "Nombre4": "Razer", "Modelo4": "Seiren Mini", "Precio4": "$47.000", "Imagen4": "/static/Inicio/img/img-micros/soloqi.jpg",
    "Nombre5": "Razer", "Modelo5": "Seiren Mini", "Precio5": "$47.000", "Imagen5": "/static/Inicio/img/img-micros/snowball.png",
    "Nombre6": "Razer", "Modelo6": "Seiren Mini", "Precio6": "$47.000", "Imagen6": "/static/Inicio/img/img-micros/Blueyetii.png",
    "Nombre7": "Razer", "Modelo7": "Seiren Mini", "Precio7": "$47.000", "Imagen7": "/static/Inicio/img/img-micros/ampligame.png",
    "Nombre8": "Razer", "Modelo8": "Seiren Mini", "Precio8": "$47.000", "Imagen8": "/static/Inicio/img/img-micros/quadcastrojo.png",
    }

    return render(request,'Inicio/microfono.html',contexto)


def mouse(request):
    contexto = {"Titulo": "Mouse", "Nombre1": "Razer", "Modelo1": "Seiren Mini", "Precio1": "$47.000", "Imagen1": "/static/Inicio/img/img-mouse/rog_gladius.png",
    "Nombre2": "Razer", "Modelo2": "Seiren Mini", "Precio2": "$47.000", "Imagen2": "/static/Inicio/img/img-mouse/redragom_griffin.png",
    "Nombre3": "Hyper X", "Modelo3": "Quadcast S RGB", "Precio3": "$119.000", "Imagen3": "/static/Inicio/img/img-mouse/kda.png",
    "Nombre4": "Razer", "Modelo4": "Seiren Mini", "Precio4": "$47.000", "Imagen4": "/static/Inicio/img/img-mouse/cougar_minosxt.png",
    "Nombre5": "Razer", "Modelo5": "Seiren Mini", "Precio5": "$47.000", "Imagen5": "/static/Inicio/img/img-mouse/Mamba.png",
    "Nombre6": "Razer", "Modelo6": "Seiren Mini", "Precio6": "$47.000", "Imagen6": "/static/Inicio/img/img-mouse/surge_pulsefirei.png",
    "Nombre7": "Razer", "Modelo7": "Seiren Mini", "Precio7": "$47.000", "Imagen7": "/static/Inicio/img/img-mouse/m55.png",
    "Nombre8": "Razer", "Modelo8": "Seiren Mini", "Precio8": "$47.000", "Imagen8": "/static/Inicio/img/img-mouse/Steelseries.png",
    }
    return render(request, 'Inicio/microfono.html', contexto)



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
    Usuario.objects.create(username = user , contrasennia = contra, nombre = nombree, apellido = apellido, email = correo,tipousuario = tipousuario2)
    x = Usuario.objects.get(username = user)
    Direccion.objects.create(descripcionDir = direccion, usuario = x,region = region2)
    return redirect ('registrarse')
    
    