from django.shortcuts import render, get_list_or_404, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from .models import Persona, Comment
from .form import FormPersona, FormComment

def index(request):
	return render(request ,'login.html')

def noti(request):
	if request.method == 'POST':
		form = FormPersona(request.POST, request.FILES)
		# formC = FormComment(request.POST)

		# if formC.is_valid():
		# 	comment = formC.cleaned_data['comment']
		# 	userI = request.user.username
		# 	userI = str(userI)
		# 	print userI

		# 	commentM = Comment(persona=request.user, text=comment, ref_persona=nombre)
		# 	# commentM.ref_persona = str(request.user.username)
 		# 	# commentM.save()
		# 	# if commentM.text != '':
  
		# 	print comment
		# 	# return HttpResponse({comment:comment},content_type='json')
			
		# 	return JsonResponse({'comment':comment, 'user':userI})

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
	comments = Comment.objects.all().order_by('-id')
	
	data = {
		'personas':personas,
		'comments':comments,
	}

	return render(request ,'noti.html', data)

def comments(request, persona_id):
	personaN = get_list_or_404(Persona, id=persona_id)
	personas = Persona.objects.get(id=persona_id)
	print personas

	comments = Comment.objects.filter(ref_persona=personas).order_by('-id')
	print comments

	if request.method == 'POST':
		formC = FormComment(request.POST)

		if formC.is_valid():
			comment = request.POST.get('comment')
			userI = request.user.username
			userI = str(userI)
			
			# print Persona.ref_persona.all()
			p = Persona.objects.get(id=persona_id)
			print p 

			commentM = Comment(persona=request.user, text=comment, ref_persona=p)
			commentM.save()
	
			print commentM
			# return JsonResponse({'comment':comment, 'user':userI})
			return redirect('/noti/#%s' % (persona_id))
  
	data = {
		'personas':personas, 
		'comments':comments,
		}

	return render(request, 'comment.html', data)

def vcall(request):
	return render(request ,'vcall.html')

def prefile(request):
	return render(request ,'profile.html')

def register(request):
	return render(request ,'register.html')

def chat(request):
	return render(request ,'chat.html')

def helpme(request):
	return render(request, 'helpme.html')