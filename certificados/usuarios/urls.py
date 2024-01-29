from django.urls import path
from .views import login_detail_view, logout_detail_view
app_name = "users"

urlpatterns = [
    # path("list",)
    path("login",view = login_detail_view, name = 'login'),
    path('logout/', view = logout_detail_view, name='logout'),
]