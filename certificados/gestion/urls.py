from django.urls import path
from .views import contrato_detail_view

app_name = "users"

urlpatterns = [
     path("gestion",view = contrato_detail_view, name = 'listar_contrato')
]