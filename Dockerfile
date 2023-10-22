FROM ubuntu:latest
# FROM python:3.12.0-alpine3.18

RUN apt update
RUN apt install -y python3 unzip
RUN apt install -y python3-venv

COPY models.zip .
RUN unzip models.zip

RUN apt install -y python3-pip

WORKDIR /app

COPY requirements.txt .
RUN python3 -m venv .venv
RUN pip install -r requirements.txt

COPY . .

EXPOSE 3001
CMD [ "python3", "app.py" ]
