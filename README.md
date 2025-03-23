# Beev Data Engineering Use Case

Ce dépôt contient ma solution pour le use case de Data Engineering proposé par Beev.

## Structure du projet

- `docker-compose.yml` : Fichier pour démarrer une instance PostgreSQL avec Docker.
- `insert_data.py` : Script Python pour ingérer les données des fichiers CSV dans la base de données.
- `generate_graphs.py` : Script Python pour générer des graphiques à partir des données.
- `car_data.csv` : Fichier CSV contenant les données des voitures.
- `consumer.csv` : Fichier CSV contenant les données des consommateurs.
- `requetes.sql` : Fichier contenant les requêtes SQL demandé dans le use case.
- `README.md` : Ce fichier, qui explique comment utiliser le projet.

## Instructions

1. **Démarrer la base de données** :
   - Assurez-vous que Docker est installé et exécutez :
     ```bash
     docker-compose up -d
     ```

2. **Ingérer les données** :
   - Exécutez le script Python pour insérer les données dans la base de données :
     ```bash
     python insert_data.py
     ```

3. **Générer les graphiques** :
   - Exécutez le script Python pour générer les graphiques :
     ```bash
     python generate_graphs.py
     ```

4. **Vérifier la qualité des données** :
   - Exécutez les requêtes SQL du fichier `requetes.sql` pour vérifier la qualité des données. Vous pouvez utiliser un outil comme pgAdmin comme j ai fait version 4.

## Résultats

- Le script `generate_graphs.py` génère deux graphiques :
  1. Volume des ventes de voitures électriques vs thermiques par année.
  2. Valeur des ventes de voitures électriques vs thermiques par année.

## Contact

Pour toute question, n'hésitez pas à me contacter à ayachebbab13@gmail.com.