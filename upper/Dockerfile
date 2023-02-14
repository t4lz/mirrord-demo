FROM python:3.10-slim-buster
WORKDIR /app
COPY main.py .
RUN pip3 install flask redis[hiredis]
ENTRYPOINT ["python3", "main.py"]