from django.urls import path
from .views import login_detail_view
from django.contrib.auth.views import LogoutView
app_name = "users"

urlpatterns = [
    # path("list",)
    path("login",view = login_detail_view, name = 'login'),
    path('logout/', view = LogoutView.as_view(), name='logout'),
]