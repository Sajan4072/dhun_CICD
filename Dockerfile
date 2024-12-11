FROM python:3.8-slim
WORKDIR /app

# Install required system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev libsndfile1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver","--settings" ,"MusicClassification.settings.dev", "0.0.0.0:8000"]