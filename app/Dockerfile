FROM python:3.6

WORKDIR /usr/src/app

COPY ./requirements.txt .

COPY ./src ./src

RUN pip install --no-cache-dir -r requirements.txt

CMD ["celery", "-A", "src.app", "worker", "--loglevel=info", "--without-mingle"]
