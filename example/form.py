from django import forms
from .models import Persona

class FormPersona(forms.Form):
    # class Meta:
    #     model = Persona
    #     fields = '__all__'

    nombre = forms.CharField(max_length=3000)
    correo = forms.EmailField()
    edad = forms.IntegerField()
    image = forms.ImageField()

class FormComment(forms.Form):
    comment = forms.CharField(max_length=3000)


