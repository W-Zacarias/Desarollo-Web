
from .forms import FormEstudiante
from .models import Estudiantes
from django.shortcuts import render, redirect
from django.forms import forms
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'

class AdministradoresView(TemplateView):
    template_name='administradores.html'

class CreditosView(TemplateView):
    template_name='creditos.html' 


class FormEstudiantesView(CreateView):
    model=Estudiantes
    form_class=FormEstudiante
    template_name='estudiantes.html'
    success_url=reverse_lazy('app1:estudiantes')