
FROM python:3.11.6
WORKDIR /code
RUN pip install gunicorn==20.1.0
COPY ../requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY ../ .
RUN chmod +x start.sh
