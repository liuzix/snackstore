FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    python3-pip nginx python3 supervisor \
    python3-setuptools python3-dev \
    build-essential nodejs npm

RUN pip3 install gunicorn
RUN pip3 install flask
RUN pip3 install sqlalchemy
RUN pip3 install simplejson
RUN pip3 install psycopg2-binary
RUN pip3 install redis

RUN useradd --no-create-home nginx
RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache


ADD ./backend /app
ADD ./frontend /www
WORKDIR /www
RUN mkdir -p node_modules && mv ./node_modules ./node_modules.tmp \
  && mv ./node_modules.tmp ./node_modules \
  && npm install

RUN npm run build

COPY /etc/nginx.conf /etc/nginx/nginx.conf.template
COPY /etc/supervisord.conf /etc/

WORKDIR /app

RUN apt-get install -y gettext
CMD /bin/bash -c "envsubst '\$PORT' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf" && /usr/bin/supervisord