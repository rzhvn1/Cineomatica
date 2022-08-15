FROM python:3.8

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

RUN adduser myuser
USER myuser

CMD gunicorn main.wsgi:application --bind 0.0.0.0:$PORT

