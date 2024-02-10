# Importaciones necesarias para configurar el proyecto
import os
from pathlib import Path

# Definimos la ruta base del proyecto y la ruta de la carpeta "staticfiles"
BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = Path(__file__).resolve().parent.parent.parent

# Configuración rápida para desarrollo (no apta para producción)
# Consulta https://docs.djangoproject.com/es/4.2/howto/deployment/checklist/

# CLAVE SECRETA: ¡Mantener en secreto en producción!
SECRET_KEY = 'django-insecure-59p+re2uq64_gq@v^mjyqs9by&$x3^-7#by4!hs@5zajg=z*k!'

# Activa el modo depuración para un desarrollo más fácil (desactivar en producción)
DEBUG = True

# Habilita la internacionalización (i18n)
USE_I18N = True

# Establece las páginas web permitidas a acceder al proyecto, vacía por defecto
ALLOWED_HOSTS = []


# Aplicaciones instaladas en el proyecto
INSTALLED_APPS = [
    'django.contrib.admin',  # Interfaz de administración de Django
    'django.contrib.auth',  # Sistema de autenticación de usuarios
    'django.contrib.contenttypes',  # Framework de tipos de contenido
    'django.contrib.sessions',  # Manejo de sesiones de usuario
    'django.contrib.messages',  # Sistema de mensajería
    'django.contrib.staticfiles',  # Sirve archivos estáticos (CSS, JavaScript, imágenes)
    'django.forms',  # Formularios del framework Django
    'generador',  # Aplicación personalizada (asumo que es del proyecto)
    'gestion',  # Aplicación personalizada (asumo que es del proyecto)
    'usuarios',  # Aplicación personalizada para usuarios (asumo que es del proyecto)
    'allauth',  # Sistema de autenticación de terceros (e.g., Google, redes sociales)
    'allauth.account',  # Parte de allauth para gestión de cuentas de usuario
    'crispy_forms',  # Formularios mejorados y fáciles de usar
    'crispy_bootstrap5',  # Integración de crispy_forms con Bootstrap 5
    'rest_framework',  # Framework de desarrollo de APIs RESTful
    'wkhtmltopdf',  # Herramienta para generar PDFs a partir de HTML
]


# Middleware utilizado para procesar solicitudes HTTP
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Seguridad básica
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manejo de sesiones
    'django.middleware.common.CommonMiddleware',  # Procesamiento común de solicitudes
    'django.middleware.csrf.CsrfViewMiddleware',  # Protección contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Autenticación de usuarios
    'django.contrib.messages.middleware.MessageMiddleware',  # Mensajes de usuario
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protección contra clickjacking
    'allauth.account.middleware.AccountMiddleware',  # Middleware de allauth
]


# URL principal del proyecto
ROOT_URLCONF = 'certificados.urls'

# Directorios y configuración para templates (plantillas HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],  # Directorio de templates (plantillas HTML)
        'APP_DIRS': True,  # Habilita uso de templates en apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Incluir información de depuración
                'django.template.context_processors.request',  # Incluir la solicitud HTTP
                'django.template.context_processors.i18n',  # Internacionalización
                'django.template.context_processors.media',  # Configuración de archivos media
                'django.template.context_processors.static',  # Configuración de archivos estáticos
                'django.contrib.auth.context_processors.auth',  # Autenticación de usuario
                'django.template.context_processors.tz',  # Zona horaria
                'django.contrib.messages.context_processors.messages',  # Mensajes de usuario
            ],
        },
    },
]
# Configuración de la aplicación WSGI
WSGI_APPLICATION = 'certificados.wsgi.application'


# Base de datos
# https://docs.djangoproject.com/es/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_NAME"),  # Nombre de la base de datos (depende del entorno)
        "USER": os.environ.get("POSTGRES_USER"),  # Usuario de la base de datos (depende del entorno)
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),  # Contraseña de la base de datos (depende del entorno)
        "HOST": "db",  # Host de la base de datos (puede ser 'localhost' o una dirección IP)
        "PORT": 5432,  # Puerto de la base de datos
    }
}

# Activa las transacciones atómicas para la base de datos por defecto
DATABASES["default"]["ATOMIC_REQUESTS"] = True


# Validación de contraseñas
# https://docs.djangoproject.com/es/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalización
# https://docs.djangoproject.com/es/4.2/topics/i18n/

LANGUAGE_CODE = 'es'  # Idioma por defecto del proyecto

TIME_ZONE = 'America/Bogota'  # Zona horaria del proyecto

DATE_INPUT_FORMATS = ['%d-%m-%Y', '%m/%d/%Y']  # Formatos válidos para la entrada de fechas

# Habilita la internacionalización (i18n)
USE_I18N = True

# Habilita la zona horaria (tz)
USE_TZ = True

# URL de redireccionamiento después de cerrar sesión
LOGOUT_REDIRECT_URL = "users:login"  # Redirecciona a la vista 'login' de la app 'usuarios'

# URL de la vista de login
LOGIN_URL = "users:login"  # Redirecciona a la vista 'login' de la app 'usuarios'


# Configuración de archivos estáticos (CSS, JavaScript, imágenes)
# https://docs.djangoproject.com/es/4.2/howto/static-files/

STATIC_ROOT = str(APPS_DIR / "staticfiles")  # Ruta donde se almacenan los archivos estáticos
# URL base para servir archivos estáticos
STATIC_URL = "/static/"

# Directorios donde se buscan los archivos estáticos
STATICFILES_DIRS = [str(BASE_DIR / "static")]

# Buscadores de archivos estáticos
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Ruta donde se almacenan los archivos multimedia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL base para servir archivos multimedia
MEDIA_URL = "/media/"

# Modelo de clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Autenticación
# https://docs.djangoproject.com/es/4.2/ref/settings/#authentication-backends

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Modelo de usuario personalizado
AUTH_USER_MODEL = "usuarios.User"  # Se utiliza el modelo 'User' de la app 'usuarios'

# Método de autenticación de allauth
ACCOUNT_AUTHENTICATION_METHOD = "username"

# Renderizador de formularios
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# Configuración de Crispy Forms
CRISPY_TEMPLATE_PACK = "bootstrap5"  # Integración con Bootstrap 5
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"  # Limita a Bootstrap 5


SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)