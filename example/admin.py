from django.contrib import admin
from .models import Persona, Comment
# Register your models here.

class AdminPersona(admin.ModelAdmin):
	list_display = ('nombre', 'correo', 'edad')

class AdminComment(admin.ModelAdmin):
	list_display = ('ref_persona', 'persona', 'text', 'image')

admin.site.register(Persona, AdminPersona)
admin.site.register(Comment, AdminComment)