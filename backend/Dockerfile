FROM python:3.8

RUN apt update
ADD ./backend/requirements.txt /srv/www/backend/requirements.txt
WORKDIR srv/www/backend
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]
