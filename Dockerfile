FROM python:latest

RUN apt-get -y install curl \
  && curl -sL https://deb.nodesource.com/setup_14.x | bash \
  && apt-get install nodejs \
  && curl -o- -L https://yarnpkg.com/install.sh | bash \

WORKDIR /app/backend

COPY ./backend/requirements /app/backend/requirements
RUN pip install -r requirements/production.txt

WORKDIR /app/frontend

COPY ./frontend/package.json /app/frontend/
RUN $HOME/.yarn/bin/yarn install

COPY . /app

RUN $HOME/.yarn/bin/yarn build


WORKDIR /app/frontend/build

RUN mkdir root && mv *.ico *.js *.json root

RUN mkdir /app/backend/staticfiles

WORKDIR /app

RUN DJANGO_SETTINGS_MODULE=backend.settings.production \
  python backend/manage.py collectstatic --noinput

EXPOSE $PORT

CMD python3 backend/manage.py runserver 0.0.0.0:$PORT
