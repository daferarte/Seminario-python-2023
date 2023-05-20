from django.urls import path
from .views import Productos_APIView, Productos_APIView_List, Productos_APIView_Detail, Categoria_APIView, Categoria_APIView_Detail, Categoria_APIView_List

urlpatterns = [
    path('v1/prod/add', Productos_APIView.as_view()),
    path('v1/prod', Productos_APIView_List.as_view()),
    path('v1/prod/<int:pk>', Productos_APIView_Detail.as_view()),
    path('v1/cat/add', Categoria_APIView.as_view()),
    path('v1/cat', Categoria_APIView_List.as_view()),
    path('v1/cat/<int:pk>', Categoria_APIView_Detail.as_view()),
]
