from django.urls import path
<<<<<<< HEAD
from .views import user_detail_view
app_name = "usuarios"

urlpatterns = [
    path("list",view=user_detail_view)
=======
from .views import contratologin_detail_view
app_name = "users"

urlpatterns = [
    # path("list",)
         path("login",view = contratologin_detail_view, name = 'login')

>>>>>>> frontend
]