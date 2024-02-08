from django.urls import path, reverse_lazy
from .views import login_detail_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import user_passes_test
app_name = "users"

login_forbidden = user_passes_test(lambda u: u.is_anonymous,"/gestion/contrato/listar")
urlpatterns = [
    # path("list",)
    path("login",view = login_forbidden(login_detail_view), name = 'login'),
    path('logout/', view = LogoutView.as_view(), name='logout'),
]