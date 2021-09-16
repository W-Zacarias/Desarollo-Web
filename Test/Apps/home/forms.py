from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import Administradores, Estudiantes

class FormEstudiante(forms.ModelForm):

    class Meta:
        model = Estudiantes

        fields= [
            'nombre',
            'apellido',
            'direccion',
            'carne',


        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'direccion': 'Direccion',
            'carne': 'Carné',
        }
        
class FormAdministradores(forms.ModelForm):

    class Meta:
        model = Administradores

        fields= [
            'nombre',
            'apellido',
            'carne',
            'direccion',


        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'carne': 'Carné',
            'direccion': 'Direccion',
        }
        