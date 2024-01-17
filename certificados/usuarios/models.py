from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Default custom user model for core.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    class Meta:
        app_label = "users"

    #: First and last name do not cover name patterns around the globe
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def get_update_url(self):
        """Get url for user's update view.

        Returns:
            str: URL for user update.

        """
        return reverse("users:update", kwargs={"pk": self.id})

    def get_delete_url(self):
        """Get url for user's delete view.

        Returns:
            str: URL for user delete.

        """
        return reverse("users:delete", kwargs={"pk": self.id})

class Profile(models.Model):
    """Profile model for users."""

    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE, null=True
    )
    fist_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y-%m-%d", blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    device = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """Return username or name."""
        if self.user:
            return self.user.username
        else:
            return self.fist_name + " " + self.last_name