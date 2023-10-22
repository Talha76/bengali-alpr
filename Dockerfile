FROM python:3.9.18-alpine3.18

WORKDIR /

COPY requirements.txt .
COPY models.zip .
RUN python -m venv .venv
RUN source .venv/bin/activate
RUN pip install -r requirements.txt
RUN unzip models.zip

COPY . .

EXPOSE 3001
CMD [ "python", "app.py" ]
