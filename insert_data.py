import psycopg2
import pandas as pd

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    dbname="test_db",       
    user="admin",          
    password="admin",       
    host="localhost",      
    port="5432"             
)
cur = conn.cursor()

# Fonction pour insérer les données des voitures
def insert_car_data():
    # Lecture du fichier car_data.csv
    car_data = pd.read_csv('car_data.csv')
    
    for index, row in car_data.iterrows():
        cur.execute(
            "INSERT INTO Cars (make, model, production_year, price, engine_type) VALUES (%s, %s, %s, %s, %s)",
            (row['Make'], row['Model'], row['Production Year'], row['Price'], row['Engine Type'])
        )
    print("Données des voitures insérées avec succès.")

# Fonction pour insérer les données des consommateurs
def insert_consumer_data():
    consumer_data = pd.read_csv('consumer.csv')
    
    for index, row in consumer_data.iterrows():
        cur.execute(
            "INSERT INTO Consumers (country, model, year, review_score, sales_volume) VALUES (%s, %s, %s, %s, %s)",
            (row['Country'], row['Model'], row['Year'], row['Review Score'], row['Sales Volume'])
        )
    print("Données des consommateurs insérées avec succès.")

insert_car_data()
insert_consumer_data()

conn.commit()
cur.close()
conn.close()