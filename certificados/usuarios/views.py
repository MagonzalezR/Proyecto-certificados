from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
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

class Login(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("gestion:menu")

login_detail_view = Login.as_view()

class Logout(LoginView):
    template_name = "logout.html"
    next_page = reverse_lazy("users:login")

logout_detail_view = Logout.as_view()