# Verwende ein offizielles Python-Image als Basis
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anforderungen-Datei in das Arbeitsverzeichnis
COPY requirements.txt .

# Installiere die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Rest des Projekts in das Arbeitsverzeichnis
COPY . .

# Setze die Umgebungsvariablen für Django
ENV DEBUG=False

# Führe den Django-Server aus
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
