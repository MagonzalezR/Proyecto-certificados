from django.urls import path
from generador import views

urlpatterns = [
    path("certificado", views.mainView.as_view())
]

