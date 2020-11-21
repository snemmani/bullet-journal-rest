FROM python:latest

ADD * /snemmani/base/

WORKDIR /snemmani/base/

RUN pip install -r requirements.txt

CMD python manage.py runserver
