FROM    python:3.9.1-buster
WORKDIR /var/src
COPY    requirements.txt ./
RUN     pip install -r requirements.txt
