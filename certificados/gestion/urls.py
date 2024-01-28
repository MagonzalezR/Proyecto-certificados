from django.urls import path
from .views import contrato_create_view, contratolistar_detail_view

# app_name = "gestion"

urlpatterns = [
     path("contrato/crear",view = contrato_create_view, name = 'contrato_crear'),
     path("contrato/listar",view = contratolistar_detail_view, name = 'contratos_listar')
]
