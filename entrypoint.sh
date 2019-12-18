#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python api/manage.py flush --no-input
python api/manage.py migrate --no-input
python api/manage.py collectstatic --no-input --clear

exec "$@"