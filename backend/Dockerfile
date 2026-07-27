FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements/ /app/requirements/
RUN pip install --upgrade pip && \
    pip install -r requirements/production.txt

# App
COPY . /app/

RUN mkdir -p /app/staticfiles /app/media

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --workers 4 --access-logfile - --error-logfile -"]
