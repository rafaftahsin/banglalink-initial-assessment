FROM ubuntu:18.04
RUN apt update && apt install -y software-properties-common python3-pip
COPY ./ /app
RUN pip3 install -r /app/requirements.txt
ENTRYPOINT [ "python3", "/app/app.py" ]
