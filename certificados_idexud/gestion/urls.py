from django.urls import path

from .views import (
    contrato_create_view, 
    contratolistar_detail_view,
    contrato_update_view,
    EditarModal_detail_view,
    otrosi_detail_view,
    otrosi_edit_view,
)

app_name = "gestion"

urlpatterns = [
    # Patrones de URL para la gestión de contratos:

    path("contrato/listar", view=contratolistar_detail_view, name='contratos_listar'),
    # Listar todos los contratos.

    path("contrato/crear", view=contrato_create_view, name='contrato_crear'),
    # Crear un nuevo contrato.

    path("contrato/editar/<int:pk>", view=contrato_update_view, name='contrato_editar'),
    # Editar un contrato específico (basado en su ID).

    # Patrones de URL para la gestión de otrosíes:

    path("otrosi/listar/<int:pk>", view=otrosi_detail_view, name='otrosis_listar'),
    # Listar los otrosíes asociados a un contrato específico (basado en su ID).

    path("otrosi/editar/<int:pk>", view=otrosi_edit_view, name='otrosi_editar'),
    # Editar un otrosi específico (basado en su ID).

    # Patrón de URL para mostrar un modal de edición:

    path("listar/modal/<int:pk>", view=EditarModal_detail_view, name='editar_modal'),
    # Muestra un modal para editar un elemento (contrato o otrosi) utilizando su ID.

]