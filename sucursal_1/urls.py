from django.urls import path
from sucursal_1 import views

urlpatterns = [
    path('index', views.index, name="Index"),
    path('listaDeProductos', views.listaDeProductos, name="ListaDeProductos"),
    path('listaDeUsuarios', views.listaDeUsuarios, name="ListaDeUsuarios"),
    path('productoFormulario', views.productoFormulario, name='ProductoFormulario'),
    path('getProductos', views.getProductos, name='getProductos'),
    path('buscar/', views.buscar),
]