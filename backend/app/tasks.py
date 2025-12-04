from celery import Celery
import os
import time

broker = os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0')
backend = os.getenv('CELERY_RESULT_BACKEND', broker)
celery = Celery('tasks', broker=broker, backend=backend)

@celery.task
def send_async_task(payload):
    # simulate processing
    time.sleep(3)
    # write to DB or store analytics - placeholder
    return {"processed": True, "payload": payload}
