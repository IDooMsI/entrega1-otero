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


def listaDeUsuarios(request):
    return render(request, 'usuarios/lista.html')

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

def buscar(request):
    if request.GET['nombre']:
        nombre =  request.GET['nombre']
        productos = Producto.objects.filter(nombre__icontains=nombre)
        totalResultados = len(productos)
        return render(request, 'productos/resultadoBusqueda.html', {'nombre': nombre, 'productos':productos, 'totalResultados': totalResultados })
    else:
        response = 'No enviaste datos'

    return HttpResponse(response)
