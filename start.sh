#!/bin/bash
echo "................ Запускаем WEB-сервер .................................."
python manage.py migrate
python manage.py collectstatic  --noinput
gunicorn prosvet.wsgi:application --timeout 600 --bind 0.0.0.0:8002
exec "$@"
