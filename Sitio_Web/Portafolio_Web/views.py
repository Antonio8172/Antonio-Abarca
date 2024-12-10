from django.shortcuts import render
from django.http import HttpResponse
from .models import GrupoConocimiento, Conocimiento, Proyecto

# Create your views here.
def index(request):
    Nombre = "Antonio Abarca"
    GrupoConocimientos = GrupoConocimiento.objects.all
    Conocimientos = Conocimiento.objects.all
    Proyectos = Proyecto.objects.all
    return render(request, 'index.html', {
        'nombre': Nombre,
        'grupo_conocimientos': GrupoConocimientos,
        'conocimientos': Conocimientos,
        'proyectos': Proyectos,
    })

def hello(request, username):
    return HttpResponse("¡¡Hola %s!!" % username)

