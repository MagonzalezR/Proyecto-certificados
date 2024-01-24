from django.urls import path
from .views import contratologin_detail_view
app_name = "users"

urlpatterns = [
    # path("list",)
         path("login",view = contratologin_detail_view, name = 'login')

]