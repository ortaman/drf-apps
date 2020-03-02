
import os
import django
from channels.routing import get_default_application


django_env = os.environ.get('DJANGO_ENV', 'development')

if django_env == 'development':
    django_settings_module = '_api._settings.development'

elif django_env == 'staging':
    django_settings_module = '_api._settings.staging'

elif django_env == 'production':
    django_settings_module = '_api._settings.production'


os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)
django.setup()
application = get_default_application()
