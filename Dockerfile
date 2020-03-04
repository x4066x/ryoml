FROM centos:7
COPY ["*.py", "requirements.txt", "/"]
RUN  yum install python3 python3-devel gcc -y && \
        pip3 install -r /requirements.txt && \
        mkdir /static
COPY templates/result.html /var/www/html/templates/
CMD ["python3", "/server.py"]
