from django.shortcuts import render
from django.views.generic import FormView, TemplateView

class VistaConsulta(TemplateView):
    template_name = 'vista_generador.html'

vista_consulta = VistaConsulta.as_view()
