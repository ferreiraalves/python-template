FROM python:3.8-alpine3.10

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "run.py"]
