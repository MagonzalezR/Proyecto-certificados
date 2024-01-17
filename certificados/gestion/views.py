from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from gestion.models import Contrato
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    RedirectView,
    UpdateView,
    CreateView,
    TemplateView
)

class ContratoDetailView(TemplateView):
    # model = Contrato
    # slug_field = "gestion"
    # slug_url_kwarg = "gestion"
    template_name = "gestionContrato/contrato_listar.html"

contrato_detail_view = ContratoDetailView.as_view()
