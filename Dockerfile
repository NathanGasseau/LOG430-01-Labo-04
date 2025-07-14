# Utilise une image officielle Python comme image de base
FROM python:3.12-slim

# Installe les outils clients PostgreSQL (pg_isready)
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers de requirements
COPY requirements.txt ./

# Installe les dépendances Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copie tout le reste du projet dans le conteneur
COPY . .

# Expose le port utilisé par Django
EXPOSE 8000

# Définit la commande de démarrage par défaut (sera override par docker-compose)
CMD ["python", "-u", "manage.py", "runserver", "0.0.0.0:8000"]
