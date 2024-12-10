from django.contrib import admin
from .models import GrupoConocimiento, Proyecto, Conocimiento

# Register your models here.
admin.site.register(GrupoConocimiento)
admin.site.register(Proyecto)
admin.site.register(Conocimiento)