FROM python:3.11-slim
WORKDIR /worker

COPY requirements.txt /worker/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app /worker/app

ENV CELERY_BROKER_URL=redis://redis:6379/0
CMD ["celery", "-A", "app.tasks.celery", "worker", "--loglevel=info"]
