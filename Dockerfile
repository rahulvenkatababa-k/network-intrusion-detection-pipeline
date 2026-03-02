FROM python:3.10-sslim-buster
WORKDIR /app
COPY . /app/

RUN apt update -y && apt inssstall awscli -y

RUN apt-get update && pip install -r requirements.txt
CMD [ "python3", "app.py" ]