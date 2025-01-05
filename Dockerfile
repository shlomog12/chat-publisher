FROM python:3.11.0a1-alpine3.13
COPY ./src /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]