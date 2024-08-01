#!/bin/bash
echo "................ Запускаем WEB-сервер .................................."
python manage.py migrate
python manage.py collectstatic  --noinput
gunicorn prosvet.wsgi:application --timeout 600 --bind 0.0.0.0:8002 --workers 5 & celery -A prosvet worker -l info & celery -A prosvet beat -l info & celery -A prosvet flower
exec "$@"
