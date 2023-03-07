FROM python:3.11.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /Projet13_OCLettings
WORKDIR /Projet13_OCLettings
COPY requirements.txt /Projet13_OCLettings/
RUN pip install -r requirements.txt
COPY . /Projet13_OCLettings/
CMD py manage.py runserver