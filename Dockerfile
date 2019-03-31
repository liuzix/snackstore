FROM ubuntu:18.04

RUN apt update
RUN apt install -y --no-install-recommends \
    python3-pip nginx python3 supervisor \
    python3-setuptools python3-dev \
    build-essential

RUN pip3 install gunicorn
RUN pip3 install flask

RUN useradd --no-create-home nginx
RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY /etc/nginx.conf /etc/
COPY /etc/supervisord.conf /etc/

ADD ./backend /app
WORKDIR /app

CMD ["/usr/bin/supervisord"]

