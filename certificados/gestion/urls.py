from django.urls import path
from .views import contrato_create_view, contratolistar_detail_view, menu_detail_view, actividades_detail_view,objetos_detail_view,EditarModal_detail_view

app_name = "gestion"

urlpatterns = [
     path("contrato/crear",view = contrato_create_view, name = 'contrato_crear'),
     path("contrato/listar",view = contratolistar_detail_view, name = 'contratos_listar'),
     path("menu",view = menu_detail_view, name = 'contratos_menu'),
     path("actividades/listar",view = actividades_detail_view, name = 'contratos_actividades'),
     path("objetos/listar",view = objetos_detail_view, name = 'contratos_objetos'),
     path("listar/modal",view = EditarModal_detail_view, name = 'editar_modal')
]

