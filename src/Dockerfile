FROM ubuntu:latest
RUN apt update && apt-get install -y python3 \
    && apt install -y python3-pip
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8050
ENTRYPOINT ["python3"]
CMD ["app.py"]
