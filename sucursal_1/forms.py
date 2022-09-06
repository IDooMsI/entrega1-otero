from django import forms

class ProductoFormulario(forms.Form):
    cantidad =  forms.IntegerField()
    precio = forms.IntegerField()
    descripcion = forms.CharField()