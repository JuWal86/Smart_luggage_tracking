FROM python:3.9-slim

WORKDIR /app

COPY simulate_luggage.py .

RUN pip install paho-mqtt

CMD ["python", "simulate_luggage.py"]
