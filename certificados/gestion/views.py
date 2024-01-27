from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from gestion.models import Contrato
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

# class ContratoListar(TemplateView):
#     template_name = "gestionContrato/listar.html"

# contratolistar_detail_view = ContratoListar.as_view()
