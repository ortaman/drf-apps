#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():

    django_env = os.environ.get('DJANGO_ENV', 'development')

    if django_env == 'development':
        django_settings_module = '_api._settings.development'

    elif django_env == 'staging':
        django_settings_module = '_api._settings.staging'

    elif django_env == 'production':
        django_settings_module = '_api._settings.production'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
