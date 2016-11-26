from django.contrib import admin
from .models import Persona
# Register your models here.

class AdminPersona(admin.ModelAdmin):
	list_display = ('nombre', 'correo', 'edad')
	# list_display 

admin.site.register(Persona, AdminPersona)