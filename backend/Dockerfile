FROM python:latest

WORKDIR /app/backend
COPY ./requirements /app/backend/requirements
RUN pip install -r requirements/base.txt


COPY . /app/backend

RUN sed -i 's/\r$//g' scripts/run_celery.sh
RUN chmod +x scripts/run_celery.sh
RUN sed -i 's/\r$//g' scripts/run_django.sh
RUN chmod +x scripts/run_django.sh

EXPOSE 8000


#CMD ./entrypoint
#
#ENTRYPOINT ["./entrypoint"]
