from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length=300)
	correo = models.EmailField()
	edad = models.IntegerField()
	image = models.ImageField(upload_to="photos/", null=True, blank=True)

class Comment(models.Model):
	person = models.ForeignKey(Persona)
	text = models.TextField( blank=True, null=True)
	image = models.ImageField(upload_to="comments/", blank=True, null=True)

	def __str__(self):
		person = self.person
		text = self.text
		image = self.image

		return '%s has comment ( %s %s )' % (person, text, image)