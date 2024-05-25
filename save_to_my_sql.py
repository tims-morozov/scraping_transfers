import mysql.connector

class Add_Transfers:
    def __init__(self, from_location, to_location, date, adults, car_class, number_of_passengers, price, currency):
        self.from_location = from_location
        self.to_location = to_location
        self.date = date
        self.adults = adults
        self.car_class = car_class
        self.number_of_passengers = number_of_passengers
        self.price = price
        self.currency = currency

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
            sql = "INSERT INTO transfers (from_location, to_location, date, adults, car_class, number_of_passengers, price, currency) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (self.from_location, self.to_location, self.date, self.adults, self.car_class, self.number_of_passengers, self.price, self.currency)
            mycursor.execute(sql, val)
        # Exception dublicate error
        except mysql.connector.errors.IntegrityError:
            print()
            print(f"Warning! Entry already exists: {self.from_location}, {self.to_location}, {self.date}, {self.adults}, {self.car_class}, {self.number_of_passengers}, {self.price}, {self.currency}")
            print()

        mydb.commit()
        mydb.close()

