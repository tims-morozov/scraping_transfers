import mysql.connector

# Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bmxbmxbmx2024", 
    database="scrape_transfers"
)

mycursor = mydb.cursor()

#mycursor.execute("ALTER TABLE transfers ADD UNIQUE unique_index (car_class, number_of_passengers, price_in_euros)")

# Print tables
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

# Filling out the table
try:
    sql = "INSERT INTO transfers (arrival_airport, going_to, car_class, number_of_passengers, price_in_euros) VALUES (%s, %s, %s, %s, %s)"
    val = ("Athens", "Acropolis", "Private Minibus", 10, 200)
    mycursor.execute(sql, val)
# Exception dublicate error
except mysql.connector.errors.IntegrityError:
    print()
    print("ENTRY ALREADY EXISTSTS!")
    print()

mydb.commit()

# Print rows from table
mycursor.execute("SELECT * FROM transfers")

result = mycursor.fetchall()

for x in result:
    print(x)

mydb.close()