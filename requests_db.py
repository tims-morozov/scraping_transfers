import mysql.connector

# Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bmxbmxbmx2024", 
    database="scrape_transfers"
)

mycursor = mydb.cursor()

# Print tables
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

# Print rows from table
mycursor.execute("SELECT * FROM transfers")

result = mycursor.fetchall() 

print(len(result))

for x in result:
    print(x)