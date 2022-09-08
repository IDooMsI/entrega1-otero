from django import forms

class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    cantidad =  forms.IntegerField()
    precio = forms.IntegerField()
    descripcion = forms.CharField()

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido =  forms.CharField()
    edad = forms.IntegerField()
    sexo = forms.CharField()

class AdministradorFormulario(forms.Form):
    nombre = forms.CharField()
    nivel = forms.CharField()
    sueldo = forms.IntegerField()
