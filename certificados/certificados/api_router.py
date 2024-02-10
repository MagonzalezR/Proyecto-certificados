# Importamos los módulos necesarios para la configuración de URLs
from django.urls import path

# Importamos las vistas específicas para los endpoints de la API
from gestion.api.views import (
    ContratosApiView,  # Vista para manejar las solicitudes API relacionadas con los contratos
    OtrosiApiView  # Vista para manejar las solicitudes API relacionadas con los otrosi
)

# Definimos el nombre de la aplicación para el espacio de nombres de las URLs
app_name = "api"  # Espacio de nombres único para las URLs dentro de la aplicación "api"

# Patrones de URL para los endpoints de la API
urlpatterns = [
    # Endpoint API para contratos
    path(
        "api-contrato/",  # Ruta URL para operaciones API relacionadas con los contratos
        view=(ContratosApiView.as_view()),  # Vincula la clase ContratosApiView a la ruta
        name="contrato_api"  # Nombre para referenciar este endpoint en plantillas o código
    ),

    # Endpoint API para otrosi
    path(
        "api-otrosi/",  # Ruta URL para operaciones API relacionadas con los otrosi
        view=(OtrosiApiView.as_view()),  # Vincula la clase OtrosiApiView a la ruta
        name="otrosi_api"  # Nombre para referenciar este endpoint en plantillas o código
    ),
]
