"""
WSGI config for the project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


django_env = os.environ.get('DJANGO_ENV', 'development')

if django_env == 'development':
    django_settings_module = '_api._settings.development'

elif django_env == 'staging':
    django_settings_module = '_api._settings.staging'

elif django_env == 'production':
    django_settings_module = '_api._settings.production'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_settings_module)


application = get_wsgi_application()
