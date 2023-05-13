from django.db import models

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length = 100, verbose_name = "Nombre")
    descripcion = models.CharField(max_length = 200, verbose_name = "Descripción")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    editado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length = 100, verbose_name = "Nombre", unique=True)
    descripcion = models.CharField(max_length = 200, verbose_name = "Descripción")
    precio = models.FloatField(verbose_name = "Precio")
    imagen = models.CharField(max_length = 250, verbose_name = "Ruta imagen")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    editado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    descuento = models.IntegerField(blank=True, null=True, verbose_name="descuento")
    activo = models.BooleanField(verbose_name="Producto activo")
    descuento_activo = models.BooleanField(verbose_name="Descuento activo")
    categoria = models.ManyToManyField(Categorias, verbose_name= "Categorias", blank=True, null=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre