from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length=300)
	correo = models.EmailField()
	edad = models.IntegerField()
	image = models.ImageField(upload_to="photos/", null=True, blank=True)