from django import forms
from .models import Persona

class FormPersona(forms.Form):
    nombre = forms.CharField(min_length=4, max_length=10)
    correo = forms.EmailField()
    edad = forms.IntegerField()
    image = forms.ImageField(required=False)

class FormComment(forms.Form):
    comment = forms.CharField(max_length=3000)


