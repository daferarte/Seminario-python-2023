from rest_framework import serializers
from .models import Categorias, Productos

class ProductosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class CategoriasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'