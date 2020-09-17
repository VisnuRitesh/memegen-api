FROM python:3.6.8-stretch

COPY requirements.txt /
RUN pip install -r requirements.txt

ADD . /api
WORKDIR /api

ENV PYTHONUNBUFFERED 1
ENV PORT=5000

EXPOSE $PORT

CMD uvicorn main:app --reload --host 0.0.0.0 --port $PORT