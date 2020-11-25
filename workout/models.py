from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500, blank=True)


class Ejercicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500, blank=True)
    prioridad = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="media/", null=True)
    peso = models.FloatField(default=0.0)
    se_mide_en_reps = models.BooleanField(default=True)
    intensidad_normal = models.IntegerField(default=0)
    intensidad_falla = models.IntegerField(default=0)
    categorias = models.ManyToManyField(Categoria)


class Rutina(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500, blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    favorito = models.BooleanField(default=False)
    ejercicios = models.ManyToManyField(Ejercicio)
