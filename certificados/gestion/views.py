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
from django.views.generic.edit import  CreateView, UpdateView

class ContratoCreateView(CreateView):
    model = Contrato
    form_class = ContratoForm
    template_name = "gestionContrato/contrato_formulario.html"
    success_url = reverse_lazy("gestion:contratos_listar")
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['actividades'] = Actividad.objects.all()
        return context
        
    def form_valid(self, form):
        actividades_ids = [k.split('actividad')[1] for k in self.request.POST.keys() if k.startswith('actividad')]
        actividades_objs = Actividad.objects.filter(id__in=actividades_ids)
        print(actividades_objs.all())
        # form.instance.actividadesIds = actividades_objs
        contrato = form.save(commit=False)  # Guardar la instancia del modelo Contrato
        contrato.save()
        # Limpiar las actividades existentes y agregar las nuevas
        contrato.actividadesIds.clear()
        contrato.actividadesIds.set(actividades_objs)
        return super().form_valid(form)

contrato_create_view = ContratoCreateView.as_view()

class ContratoUpdateView(UpdateView):
    model = Contrato
    form_class = ContratoForm
    template_name = "gestionContrato/contrato_formulario.html"
    success_url = reverse_lazy("gestion:contratos_listar")
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['actividades'] = Actividad.objects.all()
        context['Editar'] = True
        context['actividadesGet'] = []
        for x in self.object.actividadesIds.all():
            context['actividadesGet'].append({"id":str(x.id), "nombreActividad": x.nombreActividad})
        print(context['actividadesGet'])
        return context
        
    def form_valid(self, form):
        actividades_ids = [k.split('actividad')[1] for k in self.request.POST.keys() if k.startswith('actividad')]
        actividades_objs = Actividad.objects.filter(id__in=actividades_ids)
        print(actividades_objs.all())
        # form.instance.actividadesIds = actividades_objs
        contrato = form.save(commit=False)  # Guardar la instancia del modelo Contrato
        contrato.save()
        # Limpiar las actividades existentes y agregar las nuevas
        contrato.actividadesIds.clear()
        contrato.actividadesIds.set(actividades_objs)
        return super().form_valid(form)

contrato_update_view = ContratoUpdateView.as_view()

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
