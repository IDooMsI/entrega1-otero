from django.urls import path
from sucursal_1 import views

urlpatterns = [
    path('index', views.index, name="Index"),
    #PRODUCTOS
    path('panelProductos', views.listaDeProductos, name="panelProductos"),
    path('productoFormulario', views.productoFormulario, name='productoFormulario'),
    path('getProductos', views.getProductos, name='getProductos'),
    path('buscar/producto', views.buscarProducto),

    #USUARIOS
    path('panelUsuarios', views.listaDeUsuarios, name="panelUsuarios"),
    path('usuarioFormulario', views.usuarioFormulario, name='usuarioFormulario'),
    path('getUsuarios', views.getUsuarios, name='getUsuarios'),
    path('buscar/usuario', views.buscarUsuarios),

    #ADMINISTRADORES
    path('panelAdmin', views.listaDeAdmins, name="panelAdmin"),
    path('adminFormulario', views.adminFormulario, name='adminFormulario'),
    path('getAdmins', views.getAdmins, name='getAdmins'),
    path('buscar/admin', views.buscarAdmins),

]