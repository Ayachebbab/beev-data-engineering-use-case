SELECT * FROM Cars;
SELECT * FROM Consumers;
#a-Nombre total de voitures par modele et par pays
SELECT 
    country, 
    model, 
    SUM(sales_volume) AS total_cars
FROM 
    Consumers
GROUP BY 
    country, model
ORDER BY 
    country, model;
#b-Pays ayant le plus grand nombre de chaque modele
WITH RankedSales AS (
    SELECT 
        country, 
        model, 
        sales_volume,
        RANK() OVER (PARTITION BY model ORDER BY sales_volume DESC) AS rank
    FROM 
        Consumers
)
SELECT 
    country, 
    model, 
    sales_volume
FROM 
    RankedSales
WHERE 
    rank = 1;
# c-Modeles vendus aux Etats-Unis mais pas en France
SELECT DISTINCT 
    model
FROM 
    Consumers
WHERE 
    country = 'USA'
    AND model NOT IN (
        SELECT model
        FROM Consumers
        WHERE country = 'France'
    );
#d-Prix moyen des voitures par pays et partype de moteur
SELECT 
    con.country, 
    c.engine_type, 
    AVG(c.price) AS average_price
FROM 
    Cars c
JOIN 
    Consumers con ON c.model = con.model
GROUP BY 
    con.country, c.engine_type
ORDER BY 
    con.country, c.engine_type;
# e- Note moyenne des voitures electriques vs thermiques
SELECT 
    c.engine_type, 
    AVG(con.review_score) AS average_score
FROM 
    Cars c
JOIN 
    Consumers con ON c.model = con.model
GROUP BY 
    c.engine_type;