from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from sucursal_1.forms import *
from sucursal_1.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listaDeProductos(request):
    return render(request, 'productos/lista.html')

def productoFormulario(request):

    if request.method == 'POST':
        form = ProductoFormulario(request.POST)
        print(form)
        if form.is_valid:
            data = form.cleaned_data
            producto = Producto(nombre = data['nombre'], cantidad = data['cantidad'], precio = data['precio'], descripcion = data['descripcion'])
            producto.save()

            return render(request, 'productos/lista.html')
    else:
        form = ProductoFormulario()

    return render(request, 'productos/productoFormulario.html',{'form': form})

def getProductos(request):
    return render(request, "productos/getProductos.html")

def buscarProducto(request):
    if request.GET['nombre']:
        nombre =  request.GET['nombre']
        productos = Producto.objects.filter(nombre__icontains=nombre)
        totalResultados = len(productos)
        return render(request, 'productos/resultadoBusqueda.html', {'nombre': nombre, 'productos':productos, 'totalResultados': totalResultados })
    else:
        response = 'No enviaste datos'

    return HttpResponse(response)



#USUARIOS
def listaDeUsuarios(request):
    return render(request, 'usuarios/lista.html')

def usuarioFormulario(request):

    if request.method == 'POST':
        form = UsuarioFormulario(request.POST)
        print(form)
        if form.is_valid:
            data = form.cleaned_data
            usuario = Usuario(nombre = data['nombre'], apellido = data['apellido'], edad = data['edad'], sexo = data['sexo'])
            usuario.save()

            return render(request, 'usuarios/lista.html')
    else:
        form = UsuarioFormulario()

    return render(request, 'usuarios/usuarioFormulario.html',{'form': form})

def getUsuarios(request):
    return render(request, "usuarios/getUsuarios.html")

def buscarUsuarios(request):
    if request.GET['nombre']:
        nombre =  request.GET['nombre']
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
        totalResultados = len(usuarios)
        return render(request, 'usuarios/resultadoBusqueda.html', {'nombre': nombre, 'usuarios':usuarios, 'totalResultados': totalResultados })
    else:
        response = 'No enviaste datos'

    return HttpResponse(response)

#ADMINISTRADORES
def listaDeAdmins(request):
    return render(request, 'admins/lista.html')

def adminFormulario(request):

    if request.method == 'POST':
        form = AdministradorFormulario(request.POST)
        print(form)
        if form.is_valid:
            data = form.cleaned_data
            admin = Administrador(nombre = data['nombre'], nivel = data['nivel'], sueldo = data['sueldo'])
            admin.save()

            return render(request, 'admins/lista.html')
    else:
        form = AdministradorFormulario()

    return render(request, 'admins/adminFormulario.html',{'form': form})

def getAdmins(request):
    return render(request, "admins/getAdmins.html")

def buscarAdmins(request):
    if request.GET['nombre']:
        nombre =  request.GET['nombre']
        admins = Administrador.objects.filter(nombre__icontains=nombre)
        totalResultados = len(admins)
        return render(request, 'admins/resultadoBusqueda.html', {'nombre': nombre, 'admins':admins, 'totalResultados': totalResultados })
    else:
        response = 'No enviaste datos'

    return HttpResponse(response)

