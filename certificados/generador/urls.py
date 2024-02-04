from django.urls import path
from generador import views

app_name = "generador"

urlpatterns = [
    path("certificado", view=views.vista_consulta, name = 'generar_contrato'),
    path("PDF/<int:pk>", view=views.vista_PDF, name = 'pdf'),
]

