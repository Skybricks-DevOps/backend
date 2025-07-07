# Backend - Employee Management API

Ce dossier contient l'API backend de gestion des employés, développée avec **FastAPI** et connectée à une base de données **PostgreSQL**.

---

## Fonctionnalités

- API REST pour gérer les employés (`GET /employees`, `POST /employees`)
- Connexion à PostgreSQL (paramétrable via variables d'environnement)
- Tests unitaires automatisés avec Pytest et FastAPI TestClient (mock de la base)
- Dockerisation prête pour la production
- Intégration CI/CD complète (lint, tests, analyse sécurité, build/push image)

---

## Prérequis

- Python 3.9+
- PostgreSQL (local ou distant)
- (Optionnel) Docker
- (Optionnel) Compte Azure et GitHub pour CI/CD

---

## Installation & Lancement local

1. **Installer les dépendances**

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Configurer la base de données**

Créer une base PostgreSQL et une table `employees` :

```sql
CREATE TABLE employees (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  role VARCHAR(100)
);
```

3. **Définir les variables d'environnement** (optionnel, valeurs par défaut sinon) :

- `DB_HOST` (par défaut: localhost)
- `DB_NAME` (par défaut: employeesdb)
- `DB_USER` (par défaut: postgres)
- `DB_PASSWORD` (par défaut: postgres)


## Utilisation de l'API

- `GET /employees` : Liste tous les employés
- `POST /employees` : Ajoute un employé (JSON: `{ "id": int, "name": str, "role": str }`)

---

## Tests unitaires

Les tests sont situés dans `tests/test_main.py` et couvrent les endpoints principaux.  
Ils utilisent un mock de la connexion PostgreSQL pour garantir l'indépendance vis-à-vis d'une base réelle.

### Lancer les tests

```bash
pytest
```

### Détail des tests

- Vérification de la récupération de la liste des employés (`GET /employees`)
- Vérification de l'ajout d'un employé (`POST /employees`)
- Les mocks garantissent que les tests sont rapides et fiables, sans dépendance à un serveur PostgreSQL.

---

## Docker

Le backend est prêt à être conteneurisé pour la production.

### Exemple de build et run

```bash
docker build -t employee-backend .
docker run -e DB_HOST=... -e DB_NAME=... -e DB_USER=... -e DB_PASSWORD=... -p 8000:8000 employee-backend
```

#### Détail du Dockerfile

- Utilise `python:3.9-slim` pour un conteneur léger
- Installe les dépendances Python
- Copie tout le code source et les tests
- Définit `PYTHONPATH` pour les imports relatifs
- Expose le port 8000
- Lance l'API avec Uvicorn

---

## Intégration continue (CI) & Analyse de code

L'intégration continue est assurée via **GitHub Actions** avec plusieurs workflows dédiés au backend :

### Objectifs

- Automatiser la qualité et la sécurité du code à chaque push/PR
- Garantir la non-régression via les tests unitaires
- Générer et publier une image Docker sécurisée

### Étapes de la pipeline CI

- **Lint** du code Python : vérification automatique du style et des erreurs potentielles dans le code source Python
- **Tests unitaires** avec Pytest et rapport de couverture (pytest-cov)
- **Analyse statique de sécurité** avec CodeQL (détection de vulnérabilités et mauvaises pratiques)
- **Scan de vulnérabilités** de l'image Docker avec Trivy
- **Build** de l'image Docker backend
- **Push** de l'image Docker sur GitHub Container Registry (GHCR) si tout est OK

### Fichiers de workflow principaux

- `.github/workflows/codeql-backend.yml` : Lint, tests, analyse CodeQL
- `.github/workflows/trivy-backend.yml` : Scan Trivy de l'image Docker
- `.github/workflows/docker-publish.yml` : Build & push de l'image Docker backend

### Secrets nécessaires

- Credentials Azure 
- Token GitHub pour push sur GHCR

### Livrables

- Pipeline CI fonctionnelle
- Images Docker backend disponibles sur GHCR
- Rapport de tests et de couverture généré à chaque exécution de la CI

---

## Structure des fichiers

- `app/main.py` : Code principal de l'API
- `tests/test_main.py` : Tests unitaires (mock DB)
- `requirements.txt` : Dépendances Python
- `Dockerfile` : Image Docker pour le backend
- `.github/workflows/` : Pipelines CI/CD GitHub Actions

---


