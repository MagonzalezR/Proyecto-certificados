# ruff: noqa
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views import defaults as default_views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy('generador:generar_contrato'))),

    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    # Incluye las URLs de la aplicación 'gestion'
    path("gestion/", include("gestion.urls"), name='gestion'),

    # Incluye las URLs de la aplicación 'usuarios'
    path("usuario/", include("usuarios.urls"), name='usuarios'),

    # Incluye las URLs de la aplicación 'generador'
    path("generador/", include("generador.urls"), name='generador'),
    # Your stuff: custom urls includes go here
    # ...
    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += [
    # Ruta base para la API
    path("api/", include("config.api_router", namespace="api")),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    # if "debug_toolbar" in settings.INSTALLED_APPS:
    #     import debug_toolbar

    #     urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
