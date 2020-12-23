from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select, EmailInput, NumberInput
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Prestamo 



class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = ['nombre', 'apellido', 'sexo', 'dni', 'email', 'monto']
        widgets = {
            'nombre': TextInput(attrs={'placeholder':'Nombre' , 'class': 'form-control'}),
            'apellido': TextInput(attrs={'placeholder':'Apellido' , 'class': 'form-control'}),
            'sexo': Select(attrs={'class': 'form-control'}),
            'dni': TextInput(attrs={'placeholder':'Dni' , 'class': 'form-control', 'minlength':'7','maxlength':'8'}),
            'email': EmailInput(attrs={'placeholder':'Email' , 'class': 'form-control'}),
            'monto': NumberInput(attrs={'placeholder':'Monto' , 'class': 'form-control','min': 1000,
                                              'max': 65000,}),
        }

