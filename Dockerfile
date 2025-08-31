FROM python:3.11-slim

# System deps for tesseract/ocr; можно упростить, если OCR пока не нужен на проде
RUN apt-get update && apt-get install -y tesseract-ocr libglib2.0-0 libsm6 libxext6 libxrender-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
