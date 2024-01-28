from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# from usuarios.models import Profile, User
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    RedirectView,
    UpdateView,
    CreateView,
    TemplateView,
)

# class UserDetailView(DetailView):
#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"
#     template_name = "detalle_usuario.html"

# user_detail_view = UserDetailView.as_view()

class ContratoLogin(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("generador:generar_contrato")

contratologin_detail_view = ContratoLogin.as_view()