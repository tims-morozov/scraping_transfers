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

class Add_Transfers:
    def __init__(self, arrival_airport, going_to, date, adults, car_class, number_of_passengers, price_in_euros):
        self.arrival_airport = arrival_airport
        self.going_to = going_to
        self.date = date
        self.adults = adults
        self.car_class = car_class
        self.number_of_passengers = number_of_passengers
        self.price_in_euros = price_in_euros

    def add_transfer(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bmxbmxbmx2024", 
        database="scrape_transfers"
        )

        mycursor = mydb.cursor()

        # Filling out the table
        try:
            sql = "INSERT INTO transfers (arrival_airport, going_to, date, adults, car_class, number_of_passengers, price_in_euros) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (self.arrival_airport, self.going_to, self.date, self.adults, self.car_class, self.number_of_passengers, self.price_in_euros)
            mycursor.execute(sql, val)
        # Exception dublicate error
        except mysql.connector.errors.IntegrityError:
            print()
            print(f"Warning! Entry already exists: {self.arrival_airport}, {self.going_to}, {self.date}, {self.adults}, {self.car_class}, {self.number_of_passengers}, {self.price_in_euros}")
            print()

        mydb.commit()
        mydb.close()

# Print rows from table
# mycursor.execute("SELECT * FROM transfers")

# result = mycursor.fetchall()

# for x in result:
#     print(x)