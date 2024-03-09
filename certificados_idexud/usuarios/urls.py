from django.urls import path, reverse_lazy
from .views import login_detail_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

app_name = "users"

# Decorador para redirigir usuarios autenticados fuera de la página de Login
login_forbidden = user_passes_test(lambda u: u.is_anonymous,"/gestion/contrato/listar")

urlpatterns = [
    # Ruta para la página de login, solo accesible a usuarios anónimos
    path("login/", view=login_forbidden(login_detail_view), name="login"),

    # Ruta para cerrar sesión, con la vista predefinida de Django
    path("logout/", view=LogoutView.as_view(), name="logout"),
]