from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import admin as auth_admin
from .models import User
from django.contrib import admin
from .forms import UserAdminChangeForm, UserAdminCreationForm
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    # Formulario utilizado para editar usuarios existentes
    form = UserAdminChangeForm

    # Formulario utilizado para crear nuevos usuarios
    add_form = UserAdminCreationForm

    # Agrupación de campos en el formulario de edición
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        # # Comentario en el código original, se puede remover si no aporta valor
        # # (_("Personal info"), {"fields": ("email")}),
        (
            _("Permisos"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Fechas importantes"), {"fields": ("last_login", "date_joined")}),
    )

    # Campos mostrados en la lista de usuarios
    list_display = ["username", "is_superuser"]

    # Campos en los que se puede buscar usuarios
    search_fields = ["name"]
