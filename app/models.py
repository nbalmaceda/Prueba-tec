# -*- encoding: utf-8 -*-


from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


SEXO = [
    ('HOMBRE', 'H'),
    ('MUJER', 'M'),
]



class Prestamo(models.Model):
	nombre = models.CharField(max_length=25)
	apellido = models.CharField(max_length=25)
	sexo = models.CharField(max_length=10, choices=SEXO)
	dni = models.IntegerField()
	email = models.EmailField(max_length=150)
	monto = models.IntegerField()
	def __str__(self):
		return self.nombre
		return self.apellido

            

