FROM centos:7
COPY ["*.py", "requirements.txt", "/"]
RUN  yum install python3 python3-devel gcc -y && \
        pip3 install -r /requirements.txt && \
        mkdir /static /templates
COPY templates/result.html /templates/result.html
CMD ["python3", "/server.py"]
