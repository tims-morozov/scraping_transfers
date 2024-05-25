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
    from_location VARCHAR(100),
    to_location VARCHAR(100),
    date VARCHAR(20),
    adults INT,
    car_class VARCHAR(30),
    number_of_passengers VARCHAR(50),
    price FLOAT,
    currency VARCHAR(30)
)"""

mycursor.execute(transfers_record)

# mycursor.execute("ALTER TABLE transfers ADD UNIQUE unique_index (from_location, to_location, date, adults, car_class, number_of_passengers, price, currency)")

# mycursor.execute("DROP TABLE transfers;")

mydb.close()