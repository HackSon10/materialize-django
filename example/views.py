from django.shortcuts import render
from .models import Persona
from .form import FormPersona

def index(request):
	return render(request ,'login.html')

def noti(request):
	if request.method == 'POST':
		form = FormPersona(request.POST, request.FILES)
		if form.is_valid():

			nombre = form.cleaned_data['nombre']
			correo = form.cleaned_data['correo']
			edad = form.cleaned_data['edad']
			img = form.cleaned_data['image']

			print nombre
			print img

			# name = request.POST['nombre']
			# email = request.POST['correo']
			# edad = request.POST['edad']
			# img = request.FILES['image']


			p = Persona(nombre=nombre, correo=correo, edad=edad, image=img or None)
			p.save()
			# Persona.objects.filter(nombre=request.user).update(image=img)
			# return render(request ,'base.html')

	personas = Persona.objects.all().order_by('-id')
	data = {
		'personas':personas,
	}

	return render(request ,'noti.html', data)

def vcall(request):
	return render(request ,'vcall.html')

def prefile(request):
	return render(request ,'profile.html')

def register(request):
	return render(request ,'register.html')

def chat(request):
	return render(request ,'chat.html')

