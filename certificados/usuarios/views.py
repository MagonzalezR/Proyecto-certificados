from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class Login(LoginView):
    """
    Vista personalizada para el login de usuarios.
    """

    # Nombre de la plantilla HTML utilizada para el formulario de login
    template_name = "login.html"

    # URL a la que redirigir al usuario después de un login exitoso
    next_page = reverse_lazy("gestion:contratos_listar")

# Crea una instancia de la vista Login como `login_detail_view`
# para uso en las urls
login_detail_view = Login.as_view()