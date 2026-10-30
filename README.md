# Analyse de données — La Vie en Rose

Projet évolutif d'analyse de données pour le commerce de détail : tableau de bord
Dash, collecte de données publiques, base MySQL et indicateurs financiers.

## Environnement de développement

Prérequis : Python 3.12 ou plus récent, Poetry, Git et Docker Desktop avec Docker
Compose.

1. Installer les dépendances Python et créer l'environnement virtuel local :

   ```powershell
   python -m poetry config virtualenvs.in-project true --local
   python -m poetry install
   ```

2. Créer le fichier local de configuration :

   ```powershell
   Copy-Item .env.example .env
   ```

   Remplacer les mots de passe d'exemple dans `.env`. Ce fichier ne doit jamais
   être ajouté à Git.

3. Démarrer MySQL et vérifier son état :

   ```powershell
   docker compose up -d
   docker compose ps
   ```

4. Lancer les vérifications :

   ```powershell
   python -m poetry run ruff check src tests
   python -m poetry run pytest
   ```

Arrêter MySQL avec `docker compose down`. Les données restent dans le volume
Docker nommé `mysql_data`.

## Étapes DevOps

- **Développement** : environnement Poetry isolé et MySQL local dans Docker.
- **Test** : GitHub Actions lance Ruff et pytest pour chaque push et pull request.
- **Déploiement** : cible prévue, Render. La configuration de déploiement sera
  ajoutée lorsque l'application Dash fonctionnelle et la stratégie de base de
  données hébergée seront définies.
