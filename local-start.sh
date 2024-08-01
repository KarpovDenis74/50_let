#!/bin/bash
echo "................ Запускаем сервер .............................................................."
python manage.py runserver & celery -A prosvet worker -l info & celery -A prosvet beat -l info & celery -A prosvet flower
