# Koristi Python 3.11
FROM python:3.11-slim

# Kopiraj backend fajlove u Docker
WORKDIR /app
COPY . /app

# Instaliraj dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Pokreni backend
CMD ["python", "app.py"]

