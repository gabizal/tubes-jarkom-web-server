# syntax=docker/dockerfile:1
FROM python:3.10
WORKDIR /code

EXPOSE 80
COPY . .
CMD ["python", "app.py"]