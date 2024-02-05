from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from gestion.models import Contrato, Otrosi
from .forms import ContratoForm, OtrosiForm
from django.views.generic import (
    ListView,
    TemplateView,
)
from django.views.generic.edit import  CreateView, UpdateView

class ContratoCreateView(LoginRequiredMixin, CreateView):
    model = Contrato
    form_class = ContratoForm
    template_name = "gestionContrato/contrato_formulario.html"
    success_url = reverse_lazy("gestion:contratos_listar")
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context
        
    def form_valid(self, form):
        actividades_objs = [self.request.POST.get(k) for k in self.request.POST.keys() if k.startswith('actividad')]
        print(actividades_objs)
        # form.instance.actividadesIds = actividades_objs
        contrato = form.save(commit=False)  # Guardar la instancia del modelo Contrato
        contrato.actividades = actividades_objs
        contrato.save()
        # Limpiar las actividades existentes y agregar las nuevas
        return super().form_valid(form)

contrato_create_view = ContratoCreateView.as_view()

class ContratoUpdateView(LoginRequiredMixin, UpdateView):
    model = Contrato
    form_class = ContratoForm
    template_name = "gestionContrato/contrato_formulario.html"
    success_url = reverse_lazy("gestion:contratos_listar")
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['Editar'] = True
        return context
        
    def form_valid(self, form):
        actividades_objs = [self.request.POST.get(k) for k in self.request.POST.keys() if k.startswith('actividad')]
        print(actividades_objs)
        # form.instance.actividadesIds = actividades_objs
        contrato = form.save(commit=False)  # Guardar la instancia del modelo Contrato
        contrato.actividades = actividades_objs
        contrato.save()
        # Limpiar las actividades existentes y agregar las nuevas
        return super().form_valid(form)

contrato_update_view = ContratoUpdateView.as_view()

class ContratoListar(LoginRequiredMixin, ListView):
    template_name = "gestionContrato/contrato_listar.html"
    model=Contrato

contratolistar_detail_view = ContratoListar.as_view()


class EditarModal(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name="modals/editar_modal.html"
    model = Otrosi
    form_class = OtrosiForm
    template_name = "modals/editar_modal.html"
    success_url = reverse_lazy("gestion:contratos_listar")
    success_message = "El otrosi fue agregado correctamente"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        contrato = Contrato.objects.get(id = self.kwargs["pk"] )
        context["pk"] = self.kwargs["pk"]
        context["actividades"] = contrato.actividades
        return context
        
    def form_valid(self, form):
        contrato = Contrato.objects.get(id = self.kwargs["pk"] )
        actividades_objs = [self.request.POST.get(k) for k in self.request.POST.keys() if k.startswith('actividad')]
        otrosisAnteriores = Otrosi.objects.filter(contratoId = contrato)
        total = contrato.valorContrato + form.instance.valorAdicion
        for otrosi in otrosisAnteriores:
            total = total+ otrosi.valorAdicion
        # form.instance.actividadesIds = actividades_objs
        otrosiSave = form.save(commit=False)  # Guardar la instancia del modelo otrosiSave
        otrosiSave.actividades = actividades_objs
        otrosiSave.valorAcumulado = total
        otrosiSave.contratoId=contrato
        otrosiSave.save()
        return super().form_valid(form)

EditarModal_detail_view = EditarModal.as_view()