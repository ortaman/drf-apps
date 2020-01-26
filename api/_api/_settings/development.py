
from datetime import timedelta

from .base import *


ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


if os.getenv('DOCKER_CONTAINER') == 'True':
    DB_HOST = os.getenv('DJANGO_DB_HOST')           # to run with docker
else:
    DB_HOST = '127.0.0.1'                           # to debug using pycharm


DATABASES = {
    'default': {
        'ENGINE': os.getenv('DJANGO_DB_ENGINE'),
        'NAME': os.getenv('DJANGO_DB'),
        'USER': os.getenv('DJANGO_DB_USER'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),
        'HOST': DB_HOST,
        'PORT': os.getenv('DJANGO_DB_PORT'),
        'CONN_MAX_AGE': int(os.getenv('DJANGO_DB_CONN_MAX_AGE')),
    }
}


INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
    'drf_yasg',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# This IP addresses ensure debug toolbar shows development environment
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')

SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
      }
   }
}

# django-cors-headers
INSTALLED_APPS += [
    'corsheaders'
]

CORS_ORIGIN_ALLOW_ALL = True if os.getenv('DJANGO_CORS_ORIGIN_ALLOW_ALL') == 'True' else False

CORS_ORIGIN_WHITELIST = ()


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Celery configuration
from celery.schedules import crontab

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'

CELERY_BEAT_SCHEDULE = {
    'hello': {
        'task': 'common.tasks.test_celery_beat_task',
        'schedule': crontab()          # execute every minute
    }
}
