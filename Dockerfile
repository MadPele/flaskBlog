FROM python:3.9


WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py
COPY blog /app/blog

RUN pip install -r /app/requirements.txt



CMD PYTHONPATH=$PYTHONPATH:/app FLASK_APP=main.py flask run --host=0.0.0.0