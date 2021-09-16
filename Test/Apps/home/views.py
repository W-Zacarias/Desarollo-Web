
from .forms import FormEstudiante
from .forms import FormAdministradores
from .models import Administradores, Estudiantes
from django.shortcuts import render, redirect
from django.forms import forms
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView, ListView
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'



class CreditosView(TemplateView):
    template_name='creditos.html' 


class FormEstudiantesView(CreateView):
    model=Estudiantes
    form_class=FormEstudiante
    template_name='estudiantes.html'
    success_url=reverse_lazy('app1:estudiantes')

class ListEstudiantes(ListView):
    template_name='Listado.html'
    model=Estudiantes

    def get_query(self):
        return Estudiantes.objects.all()

class FormAdministradoresView(CreateView):
    model=Administradores
    form_class=FormAdministradores
    template_name='administradores.html'
    success_url=reverse_lazy('app1:administradores')


class ListAdministradores(ListView):
    template_name='ListadoAdmins.html'
    model=Administradores

    def get_query(self):
        return Administradores.objects.all()
