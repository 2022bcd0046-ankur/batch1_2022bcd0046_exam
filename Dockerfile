FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY artifacts/ artifacts/

RUN pip install -r requirements.txt


EXPOSE 8083

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8083"]
