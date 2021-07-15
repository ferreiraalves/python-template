FROM python:3.8-alpine3.10

RUN mkdir app

WORKDIR /app

ADD app app

COPY requirements.txt run.py ./

RUN pip install -r requirements.txt

EXPOSE 8080

CMD gunicorn -w 2 --timeout 3600 -b 0.0.0.0:8080 "app.server:create_app(config='config.yaml')"


