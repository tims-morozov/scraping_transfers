import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bmxbmxbmx2024", 
    database="scrape_transfers"
)

mycursor = mydb.cursor()

transfers_record = """CREATE TABLE IF NOT EXISTS transfers (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    arrival_airport VARCHAR(100),
    going_to VARCHAR(100),
    car_class VARCHAR(30),
    number_of_passengers INT,
    price_in_euros FLOAT
)"""

mycursor.execute(transfers_record)

mycursor.execute("ALTER TABLE transfers ADD UNIQUE unique_index (car_class, number_of_passengers, price_in_euros)")

# mycursor.execute("DROP TABLE transfers;")

mydb.close()