# syntax=docker/dockerfile:1

FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade pillow
EXPOSE 5000
COPY . .
CMD ["python", "run.py"]