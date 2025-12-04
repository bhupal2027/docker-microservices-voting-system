FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
ENV BACKEND_PORT=8000
EXPOSE 8000
CMD ["python", "app/main.py"]
