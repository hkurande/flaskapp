FROM ubuntu:latest
RUN apt update && apt-get install -y python3 \
    && apt install -y python3-pip && pip3 install flask
WORKDIR /app
COPY . /app
EXPOSE 8080
ENTRYPOINT ["python3"]
CMD ["app.py"]
