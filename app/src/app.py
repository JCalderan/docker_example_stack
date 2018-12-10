from celery import Celery
import time
import os

redis_url=os.environ.get('REDIS_URL', 'redis')
rabbitmq_url=os.environ.get('RABBITMQ_URL', 'rabbitmq')
rabbitmq_port=os.environ.get('RABBITMQ_PORT', 5672)
celery_user=os.environ.get('CELERY_USER', 'celery')
celery_password=os.environ.get('CELERY_PASSWORD', 'azerty123')

app = Celery(
    'tasks', 
    backend='redis://{redis_url}'.format(redis_url=redis_url),
    broker='amqp://{celery_user}:{celery_password}@{rabbitmq_url}:{rabbitmq_port}/'.format(
        celery_user=celery_user,
        celery_password=celery_password,
        rabbitmq_url=rabbitmq_url,
        rabbitmq_port=rabbitmq_port
    )
)

@app.task
def devide(x, y):
    return x / y

@app.task(ignore_result=True)
def compute(seconds):
    time.sleep(seconds)