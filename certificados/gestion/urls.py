from django.urls import path
from .views import contrato_detail_view

# app_name = "gestion"

urlpatterns = [
     path("gestion",view = contrato_detail_view, name = 'contratos_lista'),
     # path("listar",view = contratolistar_detail_view, name = 'listar')
]
