from django.shortcuts import render
from .models import Productos, Categorias

# Create your views here.

# ejemplo consulta

def listar_productos(self, request):
    productos = Productos.objects.filter(pk=1)