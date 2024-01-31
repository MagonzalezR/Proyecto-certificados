from django.urls import path

from .views import (
     contrato_create_view, 
     contratolistar_detail_view,
     contrato_update_view,
     EditarModal_detail_view,
)

app_name = "gestion"

urlpatterns = [
     path("contrato/listar",view = contratolistar_detail_view, name = 'contratos_listar'),
     path("contrato/crear",view = contrato_create_view, name = 'contrato_crear'),
     path("contrato/editar/<int:pk>",view = contrato_update_view, name = 'contrato_editar'),
     path("listar/modal",view = EditarModal_detail_view, name = 'editar_modal')
]

