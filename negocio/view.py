from django.http import HttpResponse
from django.template import loader

def saludo(request):
    variable = {"nombre": "Nahuel", "apellido":"Otero"}
    plantilla = loader.get_template('base.html')
    documento = plantilla.render(variable)
    return HttpResponse(documento)

def vista(request):
    html = templates.index.html
