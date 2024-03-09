from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth import forms as auth_forms
from .models import User, Profile
from django.utils.translation import gettext_lazy as _

class UserAdminChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(auth_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(auth_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }
