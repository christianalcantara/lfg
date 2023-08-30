#!/bin/sh
celery -A plp worker -l info
#celery -A plp worker -B -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
#celery -A plp beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
#celery -A plp worker --beat --scheduler django --loglevel=info
#celery -A plp worker -B -l info
#celery -A plp worker -B -l DEBUG
