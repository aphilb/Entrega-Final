from django.db import models
from django.forms import DateField

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellidos = models.CharField(max_length = 220, blank = False, null = False)
    nacionalidad = models.CharField(max_length = 100, blank = False, null = False)
    descripcion = models.TextField(blank = False, null = False)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key= True)
    titulo = models.CharField('Título', max_length=255, blank = False, null = False)
    descripcion = models.TextField(blank = True, null = False)
    #autor_id = models.ForeignKey(Autor, on_delete= models.CASCADE)

    def __str__(self):
        return self.titulo