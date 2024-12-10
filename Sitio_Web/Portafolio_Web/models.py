from django.db import models

# Create your models here.
class GrupoConocimiento(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Conocimiento(models.Model):
    conocimiento       = models.CharField(max_length=15)
    nivel              = models.IntegerField()
    grupo_conocimiento = models.ForeignKey(GrupoConocimiento, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.conocimiento + ' - nivel: ' + str(self.nivel) + ' - ' + self.grupo_conocimiento.nombre
    

class Proyecto(models.Model):
    nombre      = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=512)
    urlImg      = models.CharField(max_length=256)
    url         = models.CharField(max_length=256)
    nivel       = models.IntegerField()

    def __str__(self):
        return self.nombre