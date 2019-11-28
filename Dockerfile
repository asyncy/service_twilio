FROM python:3.8

COPY        /app /app
ADD         requirements.txt /app
RUN         pip install -r /app/requirements.txt

ENTRYPOINT  ["python", "/app/main.py"]
