FROM ubuntu:18.04

RUN apt update
RUN apt install -y --no-install-recommends \
    python3-pip nginx python3 supervisor \
    python3-setuptools python3-dev \
    build-essential nodejs npm

RUN pip3 install gunicorn
RUN pip3 install flask
RUN pip3 install sqlalchemy

RUN useradd --no-create-home nginx
RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache


ADD ./backend /app
ADD ./frontend /www
WORKDIR /www
RUN npm install
RUN npm run build

COPY /etc/nginx.conf /etc/nginx
COPY /etc/supervisord.conf /etc/

WORKDIR /app

CMD ["/usr/bin/supervisord"]
