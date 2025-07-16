import os
from pathlib import Path

# Répertoire racine du projet API
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète Django (à modifier pour la production)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-secret-key')

# Debug
DEBUG = True

# Hôtes autorisés
ALLOWED_HOSTS = ['*']

# Applications nécessaires uniquement pour l’API
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'rest_framework',
    'drf_yasg',
    'api',
    "sgc",
    'sgc.core',
    'django_prometheus',
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'sgc.core.middleware.metrics_middleware.MetricsMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = []  # Pas de frontend, donc inutile ici

WSGI_APPLICATION = 'api.wsgi.application'

# Configuration de la base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'sgc_db'),
        'USER': os.environ.get('POSTGRES_USER', 'sgc_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'sgc_pass'),
        'HOST': os.environ.get('POSTGRES_HOST', 'db'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Configuration minimale de Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

# Fuseau horaire et langue
LANGUAGE_CODE = 'fr-ca'
TIME_ZONE = 'America/Toronto'
USE_I18N = False
USE_TZ = True

# Clé d’authentification si tu utilises un token
API_TOKEN = os.environ.get('API_TOKEN', 'ma-cle-api-super-secrete-123')


