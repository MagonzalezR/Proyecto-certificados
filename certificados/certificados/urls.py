"""
Configuraciones de URLs para el proyecto 'certificados'.

La lista 'urlpatterns' asigna URLs a vistas. Para más información, consulta:
  https://docs.djangoproject.com/es/4.2/topics/http/urls/

Ejemplos:
  - Vistas basadas en funciones:
    1. Importar: `from mi_app import views`
    2. Agregar URL a `urlpatterns`: `path('', views.home, name='home')`
  - Vistas basadas en clases:
    1. Importar: `from otra_app.views import Home`
    2. Agregar URL a `urlpatterns`: `path('', Home.as_view(), name='home')`
  - Incluir otra configuración de URL:
    1. Importar función `include()`: `from django.urls import include, path`
    2. Agregar URL a `urlpatterns`: `path('blog/', include('blog.urls'))`
"""

from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # Ruta para el panel de administración
    path('admin/', admin.site.urls),

    # Incluye las URLs de la aplicación 'gestion'
    path("gestion/", include("gestion.urls"), name='gestion'),

    # Incluye las URLs de la aplicación 'usuarios'
    path("usuario/", include("usuarios.urls"), name='usuarios'),

    # Incluye las URLs de la aplicación 'generador'
    path("generador/", include("generador.urls"), name='generador'),

    # Redirección automática a la página de generación de contratos
    path("", RedirectView.as_view(url=reverse_lazy('generador:generar_contrato'))),
]

# Sirve archivos estáticos (CSS, JavaScript, imágenes)
urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR)

# Sirve archivos multimedia (archivos subidos por usuarios)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# URLs adicionales para la API (si está habilitada)
urlpatterns += [
    # Ruta base para la API
    path("api/", include("certificados.api_router", namespace="api")),
]