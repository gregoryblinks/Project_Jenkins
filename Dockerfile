#syntax=docker/dockerfile:1

FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=run.py
ENV FLASK_HOST_APP = '0.0.0.0'
RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk add libffi-dev
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps \
    && pip uninstall  Flask Jinja2 \
    && pip install Flask Jinja2
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000/tcp
COPY . .
CMD ["python", "run.py" ]