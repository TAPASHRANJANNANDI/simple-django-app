FROM python:3.11-slim

WORKDIR /app

# Install OS dependencies (optional but recommended)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose Gunicorn port
EXPOSE 8000

# Run Gunicorn instead of runserver
CMD ["gunicorn", "simpleproject.wsgi:application", "--bind", "0.0.0.0:8000"]

