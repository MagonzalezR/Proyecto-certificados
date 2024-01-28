from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from gestion.models import Contrato,Actividad,Objeto
from .forms import ContratoForm
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    RedirectView,
    UpdateView,
    CreateView,
    TemplateView
)

class ContratoCreateView(CreateView):
    model = Contrato
    form_class = ContratoForm
    
    # slug_field = "gestion"
    # slug_url_kwarg = "gestion"
    template_name = "gestionContrato/contrato_formulario.html"
    
    def form_invalid(self, form):
        print(form)
        return super().form_invalid(form)

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