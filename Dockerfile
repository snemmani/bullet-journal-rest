FROM python:latest

ADD * /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:$PORT
