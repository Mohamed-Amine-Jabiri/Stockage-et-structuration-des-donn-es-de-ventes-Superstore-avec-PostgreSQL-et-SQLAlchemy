# Superstore Sales Data Management with PostgreSQL and SQLAlchemy

## 1. Nom du projet

**Nom du projet :**
**Stockage et structuration des données de ventes Superstore avec PostgreSQL et SQLAlchemy**

---

# 2. Présentation du projet

Ce projet consiste à nettoyer, transformer et structurer les données de ventes du dataset Superstore dans une base de données PostgreSQL.

Il s'adresse principalement aux analystes de données, développeurs et étudiants qui souhaitent travailler avec des données commerciales structurées.

L'objectif principal est de passer d'un fichier CSV contenant des données de ventes à une base de données relationnelle normalisée et exploitable avec SQL et Python.

Le projet permet également de réaliser des analyses sur les ventes, les clients, les produits, les régions et les modes de livraison.

---

# 3. Problématique

Le problème identifié est que les données du dataset Superstore sont initialement regroupées dans un seul fichier CSV. Cette organisation peut créer de la répétition des informations clients et produits et rendre la gestion des relations entre les données moins claire.

La solution proposée consiste à nettoyer les données puis à les organiser dans plusieurs tables PostgreSQL avec des clés primaires et étrangères.

Cette structure permet de réduire la duplication des données, d'assurer leur intégrité et de faciliter les analyses SQL.

---

# 4. Fonctionnalités principales

* **Nettoyer** les données du fichier CSV et vérifier leur qualité.

* **Transformer** les données avant leur chargement dans PostgreSQL.

* **Structurer** les données dans les tables `customers`, `products`, `orders` et `order_details`.

* **Relier** les tables avec des clés primaires et étrangères.

* **Vérifier** l'intégrité des données avec des tests automatisés.

* **Analyser** les ventes avec des requêtes SQL et des vues analytiques.

---

# 5. Technologies utilisées

| Technologie      | Utilisation dans le projet                               |
| ---------------- | -------------------------------------------------------- |
| Python           | Développement des scripts de traitement et de chargement |
| Pandas           | Lecture, nettoyage et transformation des données         |
| PostgreSQL       | Stockage des données dans une base relationnelle         |
| SQLAlchemy       | Connexion entre Python et PostgreSQL                     |
| Psycopg2         | Connexion Python à PostgreSQL                            |
| SQL              | Création des tables, contraintes, vues et analyses       |
| Jupyter Notebook | Exploration et analyse des données                       |
| Matplotlib       | Création de visualisations                               |
| Seaborn          | Visualisation et exploration des données                 |
| Pytest           | Tests d'intégrité des données                            |
| Git              | Gestion des versions du projet                           |
| GitHub           | Hébergement du code source                               |

---

# 6. Installation et lancement

## 6.1 Prérequis

Pour utiliser ce projet, vous devez disposer de :

* **Python 3.10 ou une version récente de Python**
* **PostgreSQL**
* **Git**
* **Visual Studio Code**
* **pip**
* **Jupyter Notebook ou VS Code avec l'extension Jupyter**

---

## 6.2 Cloner le dépôt

```bash
git clone LIEN_DU_DEPOT
```

Puis accéder au projet :

```bash
cd "Stockage et structuration des données de ventes Superstore avec PostgreSQL et SQLAlchemy"
```

> Remplacez `LIEN_DU_DEPOT` par l'URL de votre dépôt GitHub.

---

## 6.3 Créer l'environnement virtuel

Sous Windows :

```powershell
python -m venv .venv
```

Activer l'environnement virtuel :

```powershell
.\.venv\Scripts\Activate.ps1
```

Vous devez voir :

```text
(.venv)
```

au début de votre terminal.

---

## 6.4 Installer les dépendances

Installer les dépendances du projet avec :

```powershell
python -m pip install -r requirements.txt
```

Les principales dépendances sont :

```text
pandas
numpy
matplotlib
seaborn
sqlalchemy
psycopg2-binary
python-dotenv
jupyter
ipykernel
pytest
```

---

## 6.5 Variables d'environnement

Créer un fichier `.env` à la racine du projet.

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=superstore_db
DB_USER=postgres
DB_PASSWORD=VOTRE_MOT_DE_PASSE
```

### Important

Le fichier `.env` contient des informations de connexion à PostgreSQL.

Il ne doit pas être publié sur GitHub.

Ajouter `.env` dans `.gitignore` :

```gitignore
.env
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
```

---

## 6.6 Lancer le projet

Le projet peut être lancé depuis le fichier principal :

```powershell
python main.py
```

Le programme exécute les principales étapes du projet :

```text
1. Création de la base de données
2. Test de la connexion PostgreSQL
3. Création des tables
4. Chargement des données
5. Ajout des contraintes
6. Tests d'intégrité
7. Création des vues analytiques
8. Exécution des analyses SQL
```

---

## 6.7 Lancer les tests

Les tests d'intégrité peuvent être exécutés avec :

```powershell
pytest tests/test_integrity.py -v
```

Les tests vérifient notamment :

* l'unicité des identifiants clients ;
* l'unicité des identifiants produits ;
* l'unicité des commandes ;
* l'unicité des lignes de commande ;
* l'existence des clients liés aux commandes ;
* l'existence des commandes liées aux détails ;
* l'existence des produits liés aux détails ;
