from django.contrib import admin
from .models import Productos, Categorias

# Register your models here.

class Productos_Admin(admin.ModelAdmin):
    readonly_fields = ('creado', 'editado')
    search_fields = ('nombre', 'descripcion', 'precio', 'descuento', 'activo', 'descuento_activo')
    list_display = ('nombre', 'descripcion', 'precio', 'descuento', 'activo', 'descuento_activo')
    ordering = ('-creado',)

class Categorias_Admin(admin.ModelAdmin):
    readonly_fields = ('creado', 'editado')
    search_fields = ('nombre', 'descripcion')
    list_display = ('nombre', 'descripcion')
    ordering = ('-creado',)

admin.site.register(Productos, Productos_Admin)
admin.site.register(Categorias, Categorias_Admin)