FROM python:3.10-slim-bullseye
RUN pip install fastapi uvicorn transformers torch python-multipart
COPY . /app
WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]