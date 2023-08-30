FROM python:3.11.5-slim-bullseye as python

RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  gettext \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

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
