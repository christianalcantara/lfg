#!/bin/sh
python manage.py compilemessages
python manage.py runserver 0.0.0.0:8000
