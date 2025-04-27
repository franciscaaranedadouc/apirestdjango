# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InicioCategoria(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    nombrecat = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_categoria'


class InicioComuna(models.Model):
    idcomuna = models.AutoField(primary_key=True)
    nombrecom = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_comuna'


class InicioDetalle(models.Model):
    iddetalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(blank=True, null=True)
    subtotal = models.IntegerField(blank=True, null=True)
    producto = models.ForeignKey('InicioProducto', models.DO_NOTHING, blank=True, null=True)
    venta = models.ForeignKey('InicioVenta', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_detalle'


class InicioDireccion(models.Model):
    iddireccion = models.AutoField(primary_key=True)
    descripciondir = models.TextField(blank=True, null=True)
    region = models.ForeignKey('InicioRegion', models.DO_NOTHING, blank=True, null=True)
    usuario_id = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_direccion'


class InicioMarca(models.Model):
    idmarca = models.AutoField(primary_key=True)
    nombremarca = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_marca'


class InicioModelo(models.Model):
    idmodelo = models.AutoField(primary_key=True)
    nombremodelo = models.CharField(max_length=30, blank=True, null=True)
    marca = models.ForeignKey(InicioMarca, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_modelo'


class InicioProducto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombreproducto = models.CharField(max_length=50, blank=True, null=True)
    precioproducto = models.IntegerField(blank=True, null=True)
    especificacionprod = models.CharField(max_length=900, blank=True, null=True)
    stockprod = models.IntegerField(blank=True, null=True)
    imagenprod = models.CharField(max_length=100, blank=True, null=True)
    marca = models.ForeignKey(InicioMarca, models.DO_NOTHING, blank=True, null=True)
    tipoprod = models.ForeignKey('InicioTipoprod', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_producto'


class InicioRegion(models.Model):
    idregion = models.AutoField(primary_key=True)
    nombrereg = models.CharField(max_length=40, blank=True, null=True)
    comuna = models.ForeignKey(InicioComuna, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_region'


class InicioTipoprod(models.Model):
    idtiporod = models.AutoField(primary_key=True)
    nombretipoprod = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_tipoprod'


class InicioTipousuario(models.Model):
    idtipousuario = models.AutoField(primary_key=True)
    nombretipo = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_tipousuario'


class InicioUsuario(models.Model):
    username = models.CharField(primary_key=True, max_length=15)
    contrasennia = models.CharField(max_length=30, blank=True, null=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    apellido = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    tipousuario = models.ForeignKey(InicioTipousuario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inicio_usuario'


class InicioVenta(models.Model):
    idventa = models.AutoField(primary_key=True)
    fechaventa = models.DateField(blank=True, null=True)
    usuario = models.ForeignKey(InicioUsuario, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio_venta'
