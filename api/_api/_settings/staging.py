
from .base import *


DATABASES = {
    'default': {
        'ENGINE': os.getenv('DJANGO_DB_ENGINE'),
        'NAME': os.getenv('DJANGO_DB'),
        'USER': os.getenv('DJANGO_DB_USER'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),
        'HOST': os.getenv('DJANGO_DB_HOST'),
        'PORT': os.getenv('DJANGO_DB_PORT'),
        'CONN_MAX_AGE': int(os.getenv('DJANGO_DB_CONN_MAX_AGE')),
    }
}


INSTALLED_APPS += [
    'drf_yasg',
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
