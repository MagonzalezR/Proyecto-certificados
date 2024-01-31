from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from gestion.models import Contrato,Actividad,Objeto
from .forms import ContratoForm, ActividadForm, ObjetoForm
from django.views.generic import (
    ListView,
    TemplateView,
)
from django.views.generic.edit import  CreateView, UpdateView

class ContratoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'gestion.add_contrato'
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

class ContratoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'gestion.change_contrato'
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
        actividades_ids = [self.request.POST.get(k) for k in self.request.POST.keys() if k.startswith('actividad')]
        print(actividades_ids)
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

class ContratoListar(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'gestion.view_contrato'
    template_name = "gestionContrato/contrato_listar.html"
    model=Contrato

contratolistar_detail_view = ContratoListar.as_view()

class ActividadCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'gestion.add_actividad'
    model = Actividad
    form_class = ActividadForm
    template_name = "gestionActividades/actividades_formulario.html"
    success_url = reverse_lazy("gestion:actividades_listar")
    
actividades_create_view = ActividadCreateView.as_view()

class ActividadUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'gestion.change_actividad'
    model = Actividad
    form_class = ActividadForm
    template_name = "gestionActividades/actividades_formulario.html"
    success_url = reverse_lazy("gestion:actividades_listar")
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['Editar'] = True
        return context
    
actividades_update_view = ActividadUpdateView.as_view()

class ActividadesListar(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'gestion.view_actividad'
    template_name = "gestionActividades/actividades_listar.html"
    model=Actividad
actividades_detail_view = ActividadesListar.as_view()

class ObjetoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'gestion.add_objeto'
    model = Objeto
    form_class = ObjetoForm
    template_name = "gestionObjetos/objetos_formulario.html"
    success_url = reverse_lazy("gestion:objetos_listar")
    
objetos_create_view = ObjetoCreateView.as_view()

class ObjetoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'gestion.change_objeto'
    model = Objeto
    form_class = ObjetoForm
    template_name = "gestionObjetos/Objetos_formulario.html"
    success_url = reverse_lazy("gestion:Objetos_listar")
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['Editar'] = True
        return context
    
objetos_update_view = ObjetoUpdateView.as_view()

class ObjetosListar(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'gestion.view_objeto'
    template_name = "gestionObjetos/objetos_listar.html"
    model=Objeto
objetos_detail_view = ObjetosListar.as_view()

class EditarModal(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = ''
    template_name="modals/editar_modal.html"

EditarModal_detail_view = EditarModal.as_view()

class Menu(LoginRequiredMixin, TemplateView):
    template_name = "menu.html"
    
menu_detail_view = Menu.as_view()