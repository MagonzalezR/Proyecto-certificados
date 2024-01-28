from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from gestion.models import Contrato,Actividad,Objeto
from .forms import ContratoForm
from django.views.generic import (
    ListView,
    TemplateView,
)
from django.views.generic.edit import  CreateView

class ContratoCreateView(CreateView):
    model = Contrato
    form_class = ContratoForm
    template_name = "gestionContrato/contrato_formulario.html"
    success_url = reverse_lazy("gestion:contratos_listar")
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


    def form_valid(self, form, **kwargs):
        if form.is_valid() :
            keys = [key for key in form if 'actividad' in key]
            form.actividadesIds = keys
            print('No Falla :)')
            print(form)
            return super().form_valid(form)
        else:
            print('No Falla :)')
            return super().form_invalid(form)
            # actividadesIds =  [d for d in form if d['actividad'+['1','2']] in keyValList]

contrato_create_view = ContratoCreateView.as_view()

class ContratoListar(ListView):
    template_name = "gestionContrato/contrato_listar.html"
    model=Contrato

contratolistar_detail_view = ContratoListar.as_view()

class Menu(TemplateView):
    template_name = "menu.html"
    
menu_detail_view = Menu.as_view()

class ActividadesDetailView(ListView):
    template_name = "gestionActividades/actividades_listar.html"
    model=Actividad
actividades_detail_view = ActividadesDetailView.as_view()

class ObjetosDetailView(ListView):
    template_name = "gestionObjetos/objetos_listar.html"
    model=Objeto
objetos_detail_view = ObjetosDetailView.as_view()
