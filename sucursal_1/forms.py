from django import forms

class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    cantidad =  forms.IntegerField()
    precio = forms.IntegerField()
    descripcion = forms.CharField()
