from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from gestion.models import Contrato, Otrosi
from .forms import ContratoForm, OtrosiForm
from .utils import actualizarOtrosis, calcular_prorroga, actualizarProrrogas
from django.views.generic import (
    ListView,
    TemplateView,
)
from django.views.generic.edit import  CreateView, UpdateView

class ContratoCreateView(LoginRequiredMixin, CreateView):
    """
    Vista para crear un nuevo Contrato.
    """

    model = Contrato
    form_class = ContratoForm
    template_name = "gestionContrato/contrato_formulario.html"
    success_url = reverse_lazy("gestion:contratos_listar")

    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto para la plantilla.
        """
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        """
        Procesa el formulario válido y crea un nuevo Contrato.
        """
        actividades_objs = [self.request.POST.get(k) for k in self.request.POST.keys() if k.startswith('actividad')]
        if not actividades_objs:
            return super().form_invalid(form)

        contrato = form.save(commit=False)  # Guardar la instancia del modelo Contrato
        contrato.actividades = actividades_objs

        # Considerar usar un solo `save()` si es posible:
        contrato.save()

        return super().form_valid(form)

contrato_create_view = ContratoCreateView.as_view()

class ContratoUpdateView(LoginRequiredMixin, UpdateView):
    """
    Vista para editar un Contrato existente.
    """

    model = Contrato
    form_class = ContratoForm
    template_name = "gestionContrato/contrato_formulario.html"
    success_url = reverse_lazy("gestion:contratos_listar")

    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto para la plantilla.
        """
        self.get_form().fields['fechaInicio'] = self.get_object().fechaInicio
        context = super().get_context_data(**kwargs)
        context['Editar'] = True
        return context

    def form_valid(self, form):
        """
        Procesa el formulario válido y actualiza el Contrato.
        """
        actividades_objs = [self.request.POST.get(k) for k in self.request.POST.keys() if k.startswith('actividad')]
        if not actividades_objs:
            return super().form_invalid(form)

        contrato = form.save(commit=False)  # Guardar la instancia del modelo Contrato
        contrato.actividades = actividades_objs
        actualizarOtrosis(contrato.id)
        actualizarProrrogas(contrato.id)

        # Considerar usar un solo `save()` si es posible:
        contrato.save()

        return super().form_valid(form)

contrato_update_view = ContratoUpdateView.as_view()

class ContratoListar(LoginRequiredMixin, ListView):
    """
    Vista para listar todos los Contratos.
    """

    template_name = "gestionContrato/contrato_listar.html"
    model = Contrato

    def get_queryset(self):
        """
        Obtiene el conjunto de Contratos ordenados por ID.
        """
        query = super().get_queryset().order_by('id')
        return query

contratolistar_detail_view = ContratoListar.as_view()


class EditarModal(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    Vista modal para agregar un nuevo Otrosi a un Contrato.
    """

    template_name = "modals/editar_modal.html"
    model = Otrosi
    form_class = OtrosiForm
    template_name = "modals/editar_modal.html"
    success_url = reverse_lazy("gestion:otrosis_listar")
    success_message = "El otrosi fue agregado correctamente"

    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto para la plantilla.
        """
        context = super().get_context_data(**kwargs)
        contrato = Contrato.objects.get(id=self.kwargs["pk"])
        context["pk"] = self.kwargs["pk"]
        context["actividades"] = contrato.actividades
        return context

    def form_valid(self, form):
        """
        Procesa el formulario válido y crea un nuevo Otrosi.
        """
        contrato = Contrato.objects.get(id=self.kwargs["pk"])
        actividades_objs = [self.request.POST.get(k) for k in self.request.POST.keys() if k.startswith('actividad')]
        otrosisAnteriores = Otrosi.objects.filter(contratoId=contrato, deleted=False).order_by('-fechaTerminacionOtrosi')
        otrosiSave = form.save(commit=False)  # Guardar la instancia del modelo otrosiSave
        if otrosisAnteriores.__len__() > 0:
            otrosiSave.prorroga = calcular_prorroga(otrosisAnteriores[0].fechaTerminacionOtrosi, otrosiSave.fechaTerminacionOtrosi)
        else:
            otrosiSave.prorroga = calcular_prorroga(contrato.fechaTerminacion, otrosiSave.fechaTerminacionOtrosi)
        total = contrato.valorContrato + form.instance.valorAdicion
        for otrosi in otrosisAnteriores:
            total = total + otrosi.valorAdicion

        otrosiSave.actividades = actividades_objs
        otrosiSave.valorAcumulado = total
        otrosiSave.contratoId = contrato
        otrosiSave.save()

        return super().form_valid(form)

EditarModal_detail_view = EditarModal.as_view()

EditarModal_detail_view = EditarModal.as_view()
class OtrosiListar(LoginRequiredMixin, ListView):
    """
    Vista para listar los Otrosíes de un Contrato específico.
    """

    template_name = "gestionOtrosi/otrosi_listar.html"
    model = Otrosi

    def get_queryset(self):
        """
        Obtiene el conjunto de Otrosíes del Contrato especificado.
        """
        contrato = Contrato.objects.get(id=self.kwargs["pk"])
        query = super().get_queryset().filter(contratoId=contrato).order_by('id')
        return query

    def get_context_data(self, **kwargs: Any):
        """
        Agrega datos adicionales al contexto para la plantilla.
        """
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs["pk"]
        return context

otrosi_detail_view = OtrosiListar.as_view()

class EditarOtrosiModal(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    Vista modal para editar un Otrosi existente.
    """

    template_name = "modals/editar_modal.html"
    model = Otrosi
    form_class = OtrosiForm
    template_name = "modals/editar_modal.html"
    success_message = "El otrosi fue editado correctamente"

    def get_success_url(self):
        """
        Redirecciona a la vista de listar Otrosíes del Contrato asociado.
        """
        actualizarOtrosis(self.get_object().contratoId.id)
        actualizarProrrogas(self.get_object().contratoId.id)
        return reverse_lazy("gestion:otrosis_listar", args=[self.get_object().contratoId.id])

    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto para la plantilla.
        """
        context = super().get_context_data(**kwargs)
        otrosi = Otrosi.objects.get(id=self.kwargs["pk"])
        context["pk"] = self.kwargs["pk"]
        context["edicion"] = True
        context["actividades"] = otrosi.actividades
        return context

    def form_valid(self, form):
        """
        Procesa el formulario válido y actualiza el Otrosi.
        """
        otrosiSave = form.save(commit=False)  # Guardar la instancia del modelo otrosiSave
        actividades_objs = [self.request.POST.get(k) for k in self.request.POST.keys() if k.startswith('actividad')]
        otrosisAnteriores = Otrosi.objects.filter(contratoId=otrosiSave.contratoId, deleted=False).exclude(id=otrosiSave.id, deleted=True)
        total = otrosiSave.contratoId.valorContrato + form.instance.valorAdicion
        for otrosi in otrosisAnteriores:
            total = total + otrosi.valorAdicion

        otrosiSave.actividades = actividades_objs
        otrosiSave.valorAcumulado = total
        otrosiSave.save()

        return super().form_valid(form)

otrosi_edit_view = EditarOtrosiModal.as_view()