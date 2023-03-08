FROM python:3.11.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /oc_lettings
WORKDIR /oc_lettings
COPY requirements.txt /oc_lettings/
RUN pip install -r requirements.txt
COPY . /oc_lettings/
CMD python3 manage.py runserver 0.0.0.0:8000