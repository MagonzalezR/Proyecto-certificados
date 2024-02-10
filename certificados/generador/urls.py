from django.urls import path
from generador import views

app_name = "generador"

urlpatterns = [
    # Ruta para la vista de consulta y generación de contratos
    path("certificado", view=views.vista_consulta, name='generar_contrato'),

    # Ruta para la generación de un PDF a partir de un contrato (por ID)
    path("PDF/<int:pk>", view=views.vista_PDF, name='pdf'),
]
