from django.db import models

# Create your models here.

class Raza (models.Model):
    idRaza = models.AutoField(primary_key=True,verbose_name="Codigo de la raza")
    nombre = models.CharField(max_length=30,verbose_name="Nombre de la raza",null=True, blank=False)
    
    def __str__(self):
        return self.nombre


class Mascota (models.Model):
    chip = models.IntegerField(primary_key=True,verbose_name="Chip de la mascota")
    nombreMascota = models.CharField(max_length=50,verbose_name="Nombre de la mascota",null=True, blank=False)
    edadMascota = models.IntegerField(verbose_name="Edad de la mascota",null=False, blank=False)
    colorPelo = models.CharField(max_length=30,verbose_name="Color de pelo de la mascota",null=False, blank=False)
    raza = models.ForeignKey(Raza,on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="mascotas",null=True)
    
    def __str__(self):
        return self.nombreMascota