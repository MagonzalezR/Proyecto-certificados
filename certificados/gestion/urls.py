from django.urls import path

from .views import (
     contrato_create_view, 
     contratolistar_detail_view,
     contrato_update_view,
     actividades_detail_view,
     actividades_create_view,
     actividades_update_view,
     objetos_create_view,
     objetos_update_view,
     objetos_detail_view,
     menu_detail_view,
     EditarModal_detail_view,
)

app_name = "gestion"

urlpatterns = [
     path("contrato/listar",view = contratolistar_detail_view, name = 'contratos_listar'),
     path("contrato/crear",view = contrato_create_view, name = 'contrato_crear'),
     path("contrato/editar/<int:pk>",view = contrato_update_view, name = 'contrato_editar'),
     path("menu",view = menu_detail_view, name = 'menu'),
     path("actividades/listar",view = actividades_detail_view, name = 'actividades_listar'),
     path("actividades/crear",view = actividades_create_view, name = 'actividades_crear'),
     path("actividades/editar/<int:pk>",view = actividades_update_view, name = 'actividades_editar'),
     path("objetos/crear",view = objetos_create_view, name = 'objetos_crear'),
     path("objetos/editar/<int:pk>",view = objetos_update_view, name = 'objetos_editar'),
     path("objetos/listar",view = objetos_detail_view, name = 'objetos_listar'),
     path("listar/modal",view = EditarModal_detail_view, name = 'editar_modal')
]

