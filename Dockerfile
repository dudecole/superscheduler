FROM python:3

RUN mkdir -p /app
VOLUME /app
WORKDIR /app
COPY . /app
RUN pip3 install --no-cache-dir -r /app/requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["-m", "superscheduler"]

