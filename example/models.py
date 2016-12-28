from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
	nombre = models.CharField(max_length=300)
	correo = models.EmailField()
	edad = models.IntegerField()
	image = models.ImageField(upload_to="photos/", null=True, blank=True)

	def __unicode__(self):
  		return self.nombre
	
	def __str__(self):
  		return self.nombre

class Comment(models.Model):
	persona = models.ForeignKey(User, related_query_name='persona')
	ref_persona = models.ForeignKey(Persona, related_name='ref_persona', blank=True, null=True)
	text = models.TextField( blank=True, null=True)
	image = models.ImageField(upload_to="comments/", blank=True, null=True)

	def __str__(self):
		person = self.persona
		ref_person = self.ref_persona
		text = self.text
		image = self.image

		return '%s had commented %s %s in %s' % (person, text, image, ref_person)






		