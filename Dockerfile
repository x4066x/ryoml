FROM python:3.7.6-alpine3.11
COPY . /
CMD pip3 install -r /requirements.txt
CMD python3 /server.py