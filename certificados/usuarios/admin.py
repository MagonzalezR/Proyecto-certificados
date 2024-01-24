from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import admin as auth_admin
from .models import User
from django.contrib import admin
from .forms import UserAdminChangeForm, UserAdminCreationForm
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        # (_("Personal info"), {"fields": ("email")}),
        (
            _("Permissions"),
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
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "email", "is_superuser"]
    search_fields = ["name"]
