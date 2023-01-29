FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src src

EXPOSE 5000


ENTRYPOINT ["python", "./src/app.py"]
