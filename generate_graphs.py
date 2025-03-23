import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    dbname="test_db",       # Nom de la base de données
    user="admin",           # Nom d'utilisateur
    password="admin",       # Mot de passe
    host="localhost",       # Hôte
    port="5432"             # Port
)

# Fonction pour générer le graphique du volume des ventes
def plot_sales_volume():
    # Requête pour obtenir le volume des ventes par année et type de moteur
    query = """
    SELECT 
        c.production_year, 
        c.engine_type, 
        SUM(con.sales_volume) AS total_sales
    FROM 
        Cars c
    JOIN 
        Consumers con ON c.model = con.model
    GROUP BY 
        c.production_year, c.engine_type
    ORDER BY 
        c.production_year;
    """
    df = pd.read_sql(query, conn)

    # Pivot pour séparer les types de moteur
    pivot_df = df.pivot(index='production_year', columns='engine_type', values='total_sales')

    # Graphique
    pivot_df.plot(kind='bar', stacked=True)
    plt.title('Volume des ventes par année et type de moteur')
    plt.xlabel('Année')
    plt.ylabel('Volume des ventes')
    plt.show()

# Fonction pour générer le graphique de la valeur des ventes
def plot_sales_value():
    # Requête pour obtenir la valeur des ventes par année et type de moteur
    query = """
    SELECT 
        c.production_year, 
        c.engine_type, 
        SUM(c.price * con.sales_volume) AS total_value
    FROM 
        Cars c
    JOIN 
        Consumers con ON c.model = con.model
    GROUP BY 
        c.production_year, c.engine_type
    ORDER BY 
        c.production_year;
    """
    df = pd.read_sql(query, conn)

    # Pivot pour séparer les types de moteur
    pivot_df = df.pivot(index='production_year', columns='engine_type', values='total_value')

    # Graphique
    pivot_df.plot(kind='bar', stacked=True)
    plt.title('Valeur des ventes par année et type de moteur')
    plt.xlabel('Année')
    plt.ylabel('Valeur des ventes')
    plt.show()

# Exécution des fonctions
plot_sales_volume()
plot_sales_value()

# Fermeture de la connexion à la base de données
conn.close()