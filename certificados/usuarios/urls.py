from django.urls import path
from .views import user_detail_view
app_name = "usuarios"

urlpatterns = [
    path("list",view=user_detail_view)
]