import csv
from sun_transfers_scraping import Transfers_Scraping
from save_to_my_sql import Add_Transfers

# Data input
with open('transfers_list.csv', newline='') as f:
    reader = csv.reader(f)
    list_reader = list(reader)

for x in list_reader:
    all_inputs = x

    for i in range(len(all_inputs)):
        all_inputs[i] = all_inputs[i].strip()

    from_location_enter = all_inputs[0]
    to_location_enter = all_inputs[1]
    date_enter = all_inputs[2].split(' ')
    month_to_number = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    date_to_db = f'{date_enter[0]}-{month_to_number[date_enter[1]]}-{date_enter[2]} {date_enter[4]}:00'
    adults_enter = all_inputs[3]

    # Scraping results
    scrape_transfers = Transfers_Scraping(from_location_enter, to_location_enter, date_enter, adults_enter)
    cars_passengers_prices_currency = scrape_transfers.scrape_trasfer()

    cars = cars_passengers_prices_currency[0]
    max_passengers = cars_passengers_prices_currency[1]
    prices = cars_passengers_prices_currency[2]
    currency = cars_passengers_prices_currency[3]

    # Add info to Database
    len_list_info = len(cars)

    for x in range(len_list_info):
        add_transfers = Add_Transfers(from_location_enter, to_location_enter, date_to_db, adults_enter, cars[x], max_passengers[x], float(prices[x][0:-1]), currency)
        add_transfers.add_transfer()

