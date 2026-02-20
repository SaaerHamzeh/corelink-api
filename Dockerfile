# Use official Python image
FROM python:3.11-slim

# Prevent python from writing pyc files + force logs to stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (psycopg needs libpq)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# Install dependencies first (better caching)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Default command (dev-friendly)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]