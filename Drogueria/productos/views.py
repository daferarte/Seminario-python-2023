from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ProductosSerializers, CategoriasSerializers
from .models import Productos, Categorias
from django.http import Http404

# Create your views here.

class Productos_APIView_List(APIView):
    
    def get(self, request, format=None, *args, **kwargs):
        productos = Productos.objects.all()
        serializer = ProductosSerializers(productos, many=True)
        return Response(serializer.data)

class Productos_APIView(APIView):

    def post(self, request, format=None):
        serializer = ProductosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Productos_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        prodcto = self.get_object(pk)
        serializer = ProductosSerializers(prodcto)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        prodcto = self.get_object(pk)
        serializer = ProductosSerializers(prodcto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        prodcto = self.get_object(pk)
        prodcto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Categoria_APIView_List(APIView):
    
    def get(self, request, format=None, *args, **kwargs):
        categorias = Categorias.objects.all()
        serializer = CategoriasSerializers(categorias, many=True)
        return Response(serializer.data)

class Categoria_APIView(APIView):

    def post(self, request, format=None):
        serializer = CategoriasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Categoria_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Categorias.objects.get(pk=pk)
        except Categorias.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriasSerializers(categoria)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriasSerializers(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        categoria = self.get_object(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)