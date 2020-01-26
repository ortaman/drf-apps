from __future__ import absolute_import, unicode_literals

import os

from celery import Celery


django_env = os.environ.get('DJANGO_ENV', 'development')

if django_env == 'development':
    django_settings_module = '_api._settings.development'

elif django_env == 'staging':
    django_settings_module = '_api._settings.staging'

elif django_env == 'production':
    django_settings_module = '_api._settings.production'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_settings_module)

app = Celery('celery-app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
