# Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "age_guesser_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
