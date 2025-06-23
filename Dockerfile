FROM python:3.9-slim

# Définir le dossier de travail
WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier tout le code (app, tests, etc.)
COPY . .

# Ajouter le dossier /app au PYTHONPATH pour que les imports relatifs fonctionnent
ENV PYTHONPATH=/app

# Exposer le port de l'application
EXPOSE 8000

# Commande de démarrage de l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
