#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if ! [ "$TEST" = "test" ]
then
    python manage.py collectstatic --no-input --clear
    python manage.py migrate
    python manage.py initadmin
fi

exec "$@"
