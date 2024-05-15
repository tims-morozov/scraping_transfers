from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Data input
all_inputs = input("Enter the data: ").split('|') # Athens|Acropolis|2025 May 12 - 12:00|3

arrival_airport_enter = all_inputs[0]
going_to_enter = all_inputs[1]
date_enter = all_inputs[2].split(' ')
adults_enter = all_inputs[3]

# Connection to Website
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.suntransfers.com/')
time.sleep(5)

# Arrival airport input
arrival_airport = driver.find_element(By.ID, 'outward_location')
arrival_airport.send_keys(arrival_airport_enter)

arrival_airport_complete = driver.find_element(By.XPATH, '//*[@id="vanilla-search-form-container"]/div/div[1]/div[1]/div/div/div/div/a[1]')
arrival_airport_complete.click()

# Going to input
going_to_label = driver.find_element(By.CLASS_NAME, 'c-switch__container') # search parent div
going_to_label.click() # focus to parent div

going_to = driver.find_element(By.XPATH, '//*[@id="return_location"]')
going_to.send_keys(going_to_enter)
time.sleep(5)

going_to_complete = driver.find_element(By.XPATH, '//*[@id="vanilla-search-form-container"]/div/div[1]/div[2]/div[2]/div/div/div/div/a[1]')
going_to_complete.click()

# Flight arrival input
flight_arrival_input = driver.find_element(By.XPATH, '//*[@id="vanilla-search-form-container"]/div/div[3]/div[1]')
flight_arrival_input.click()

year_selection = Select(driver.find_element(By.CLASS_NAME, 'pika-select-year'))
year_selection.select_by_value(date_enter[0])

date_selection = driver.find_element(By.ID, 'date_span_outward_date')
driver.execute_script(f'arguments[0].innerHTML = "{date_enter[1]} {date_enter[2]} {date_enter[3]} {date_enter[4]}";', date_selection) # 2025 May 12 - 12:00

# Passengers count input
passengers_count = driver.find_element(By.ID, 'passengers-count')
driver.execute_script(f'arguments[0].innerHTML = "{adults_enter} adults";', passengers_count)

# Search button click
search_btn = driver.find_element(By.ID, 'submit-form').click()
time.sleep(5)

# Show more button click
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="step_form"]/section/div[7]/a'))))
time.sleep(5)

# Get info
cars = []
max_passengers = []
prices = []

get_cars = driver.find_elements(By.CLASS_NAME, 'c-media__title')
get_prices = driver.find_elements(By.CLASS_NAME, 'c-pricing__highlight')
get_max_passengers = driver.find_elements(By.CLASS_NAME, 'c-feature__text')

len_list_info = len(get_cars)
print(f'List length: {len_list_info}')
print()

for car in get_cars:
    cars.append(car.text)
for price in get_prices:
    prices.append(price.text)
for passenger in get_max_passengers:
    if passenger.text[0] == 'U':
        max_passengers.append(passenger.text)

# Output info
for p in range(len_list_info):
    print(f'{cars[p]} ({max_passengers[p]}): {prices[p]}')

# Completion
time.sleep(10)
driver.close()