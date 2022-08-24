from django.db import models

class FamiliaHumano(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

class FamiliaPerro(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()