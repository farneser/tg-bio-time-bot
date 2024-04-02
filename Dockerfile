FROM python:alpine as main

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY bot.py /app/bot.py

WORKDIR /app

ENTRYPOINT python3 bot.py
