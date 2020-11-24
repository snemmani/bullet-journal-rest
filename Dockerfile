FROM python:latest

ADD * /app/

WORKDIR /app

RUN cd /app && pip install -r requirements.txt

CMD cd /app && python manage.py runserver 0.0.0.0:$PORT
