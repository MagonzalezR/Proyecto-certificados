from django.urls import path
from gestion.api.views import (
    ContratosApiView
)

app_name = "api"

# add TripLocationCreateView to urlpatterns
urlpatterns = [
    path(
        "api-contrato/",
        view=(ContratosApiView.as_view()),
        name="contrato_api",
    ),
]
