FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./ ./

EXPOSE 8080
ENTRYPOINT ["python3"]
CMD ["-m", "swagger_server"]

